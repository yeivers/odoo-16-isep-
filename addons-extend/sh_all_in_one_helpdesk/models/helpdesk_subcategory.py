# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.

from odoo import models, fields, api


class HelpdeskSubCategory(models.Model):
    _name = 'helpdesk.subcategory'
    _description = 'Helpdesk SubCategory'
    _rec_name = 'name'

    sequence = fields.Integer(string="Sequence")
    name = fields.Char(required=True, translate=True,
                       string='Sub Category Name')
    parent_category_id = fields.Many2one(
        'helpdesk.category', required=True, string="Parent Category")

    @api.model_create_multi
    def create(self, values):
        sequence = self.env['ir.sequence'].next_by_code('helpdesk.subcategory')
        for value in values:
            value['sequence'] = sequence
        return super(HelpdeskSubCategory, self).create(values)
