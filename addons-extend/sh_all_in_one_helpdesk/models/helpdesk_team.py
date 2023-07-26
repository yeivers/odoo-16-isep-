# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.

from odoo import models, fields
import ast

class HelpdeskTeam(models.Model):
    _name = 'sh.helpdesk.team'
    _description = 'Helpdesk Team'
    _inherit = ['mail.alias.mixin']
    _rec_name = 'name'

    name = fields.Char('Name', required=True,translate=True)
    team_head = fields.Many2one('res.users', 'Team Head', required=True,domain=['|',('share','=',False),('sh_portal_user_access','!=',False)])
    team_members = fields.Many2many('res.users', string="Team Members",domain=['|',('share','=',False),('sh_portal_user_access','!=',False)])
    sh_resource_calendar_id = fields.Many2one('resource.calendar',string="Working Schedule",required=True,default=lambda self: self.env.company.resource_calendar_id)
    sla_count = fields.Integer(compute='_compute_helpdesk_sla')
    alias_id = fields.Many2one(
        'mail.alias', string='Alias', ondelete="restrict", required=True,
        help="The email address associated with this channel. New emails received will automatically create new tickets assigned to the team.")
    alias_user_id = fields.Many2one(
        'res.users', related='alias_id.alias_user_id', inherited=True,
        domain=lambda self: [('groups_id', 'in', self.env.ref('sh_all_in_one_helpdesk.helpdesk_group_user').id)])

    def _alias_get_creation_values(self):
        values = super(HelpdeskTeam, self)._alias_get_creation_values()
        values['alias_model_id'] = self.env['ir.model']._get('sh.helpdesk.ticket').id
        values['alias_defaults'] = defaults = ast.literal_eval(self.alias_defaults or "{}")
        defaults['team_id'] = self.id
        return values
    
    def write(self, vals):
        if vals.get('alias_name'):
            alias_vals = self._alias_get_creation_values()
            vals.update({
                'alias_name': alias_vals.get('alias_name', vals.get('alias_name')),
                'alias_defaults': alias_vals.get('alias_defaults'),
            })
        return super(HelpdeskTeam, self).write(vals)

    def _compute_helpdesk_sla(self):
        for record in self:
            record.sla_count = 0
            slas = self.env['sh.helpdesk.ticket'].sudo().search(
            [('team_id', '=', record.id),('sh_sla_status_ids','!=',False)])
            record.sla_count = len(slas.ids)
    
    def action_view_sla(self):
        self.ensure_one()
        slas = self.env['sh.helpdesk.ticket'].sudo().search(
            [('team_id', '=', self.id),('sh_sla_status_ids','!=',False)])
        action = self.env["ir.actions.actions"]._for_xml_id(
            "sh_all_in_one_helpdesk.sh_helpdesk_ticket_action")
        if len(slas) > 1:
            action['domain'] = [('id', 'in', slas.ids)]
        elif len(slas) == 1:
            form_view = [
                (self.env.ref('sh_all_in_one_helpdesk.sh_helpdesk_ticket_form_view').id, 'form')]
            if 'views' in action:
                action['views'] = form_view + \
                    [(state, view)
                     for state, view in action['views'] if view != 'form']
            else:
                action['views'] = form_view
            action['res_id'] = slas.id
        else:
            action = {'type': 'ir.actions.act_window_close'}
        return action