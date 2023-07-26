# -*- coding: utf-8 -*-

from lxml import etree
from lxml.builder import E

from odoo import _, api, fields, models

from odoo.addons.base.models.ir_model import MODULE_UNINSTALL_FLAG
from odoo.addons.base.models.res_users import name_boolean_group, name_selection_groups


class res_groups(models.Model):
    """
    Re write to update xml view of security roles
    """
    _inherit = "res.groups"

    @api.model
    def _update_user_groups_view(self):
        """
        Re-write to update view of security role
        """
        super(res_groups, self)._update_user_groups_view()
        self._update_security_role_view()

    @api.model
    def _update_security_role_view(self):
        """
        The method to prepare the view of rights the same as a user form view (mostly copied as for users view in base)
        """
        self = self.with_context(lang=None)
        view = self.sudo().env.ref("security_user_roles.security_groups_view", raise_if_not_found=False)
        if not (view and view.exists() and view._name == "ir.ui.view"):
            return

        if self._context.get("install_filename") or self._context.get(MODULE_UNINSTALL_FLAG):
            xml = E.field(name="group_ids", position="after")
        else:
            group_no_one = view.env.ref("base.group_no_one")
            group_employee = view.env.ref("base.group_user")
            xml0, xml1, xml3, xml4 = [], [], [], []
            xml_by_category = {}
            xml1.append(E.separator(string="User Type", colspan="2", groups="base.group_no_one"))

            user_type_field_name = ""
            user_type_readonly = str({})
            sorted_tuples = sorted(
                self.get_groups_by_application(),
                key=lambda t: t[0].xml_id != "base.module_category_user_type"
            )
            for app, kind, gs, category_name in sorted_tuples:
                attrs = {}
                if app.xml_id in self._get_hidden_extra_categories():
                    attrs["groups"] = "base.group_no_one"

                if app.xml_id == "base.module_category_user_type":
                    field_name = name_selection_groups(gs.ids)
                    xml0.append(E.field(name=field_name, invisible="1", on_change="1"))
                    user_type_field_name = field_name
                    user_type_readonly = str({"readonly": [(user_type_field_name, "!=", group_employee.id)]})
                    attrs["widget"] = "radio"
                    attrs["on_change"] = "1"
                    xml1.append(E.field(name=field_name, **attrs))
                    xml1.append(E.newline())

                elif kind == "selection":
                    field_name = name_selection_groups(gs.ids)
                    attrs["attrs"] = user_type_readonly
                    attrs["on_change"] = "1"
                    if category_name not in xml_by_category:
                        xml_by_category[category_name] = []
                        xml_by_category[category_name].append(E.newline())
                    xml_by_category[category_name].append(E.field(name=field_name, **attrs))
                    xml_by_category[category_name].append(E.newline())
                else:
                    app_name = app.name or "Other"
                    xml4.append(E.separator(string=app_name, **attrs))
                    left_group, right_group = [], []
                    attrs["attrs"] = user_type_readonly
                    group_count = 0
                    for g in gs:
                        field_name = name_boolean_group(g.id)
                        dest_group = left_group if group_count % 2 == 0 else right_group
                        if g == group_no_one:
                            dest_group.append(E.field(name=field_name, invisible="1", **attrs))
                        else:
                            dest_group.append(E.field(name=field_name, **attrs))
                        group_count += 1
                    xml4.append(E.group(*left_group))
                    xml4.append(E.group(*right_group))

            xml4.append({"class": "o_label_nowrap"})
            if user_type_field_name:
                user_type_attrs = {"invisible": [(user_type_field_name, "!=", group_employee.id)]}
            else:
                user_type_attrs = {}

            for xml_cat in sorted(xml_by_category.keys(), key=lambda it: it[0]):
                master_category_name = xml_cat[1]
                xml3.append(E.group(*(xml_by_category[xml_cat]), string=master_category_name))

            xml = E.field(
                *(xml0),
                E.group(*(xml1), groups="base.group_no_one"),
                E.group(*(xml3), attrs=str(user_type_attrs)),
                E.group(
                    *(xml4), 
                    attrs=str(user_type_attrs), 
                    groups="base.group_no_one"), 
                    name="group_ids", 
                    position="replace"
                )
            xml.addprevious(etree.Comment("GENERATED AUTOMATICALLY BY SECURITY USER ROLES"))

        xml_content = etree.tostring(xml, pretty_print=True, encoding="unicode")
        if xml_content != view.arch:
            new_context = dict(view._context)
            new_context.pop("install_filename", None)
            new_context["lang"] = None
            view.with_context(new_context).write({"arch": xml_content})
            # to trigger user rights update
            all_roles = self.env["security.role"].search([])
            all_roles.with_context(force_roles_update=True).write({})

