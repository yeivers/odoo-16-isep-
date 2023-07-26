# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.

from odoo import models, fields


class HelpdeskSLAPolicies(models.Model):
    _name = 'sh.helpdesk.sla'
    _description = 'Helpdesk SLA Policies'

    def get_deafult_company(self):
        company_id = self.env.company
        return company_id

    name = fields.Char('Name',required=True)
    sh_team_id = fields.Many2one('sh.helpdesk.team','Helpdesk Team',required=True)
    sh_ticket_type_id = fields.Many2one('sh.helpdesk.ticket.type','Helpdesk Team Type')
    sh_sla_target_type = fields.Selection([('reaching_stage','Reaching Stage'),('assign_to','Assigned To')],default='reaching_stage',string='SLA Target Type')
    sh_stage_id = fields.Many2one('helpdesk.stages',string='Reach Stage')
    sh_days = fields.Integer('Days',required=True)
    sh_hours = fields.Integer('Hours',required=True)
    sh_minutes = fields.Integer('Minutes',required=True)
    company_id = fields.Many2one(
        'res.company', string="Company", default=get_deafult_company)
    sla_ticket_count = fields.Integer(compute='_compute_sh_helpdesk_ticket_sla')
    
    def _compute_sh_helpdesk_ticket_sla(self):
        for record in self:
            record.sla_ticket_count = 0
            tickets = self.env['sh.helpdesk.ticket'].search(
                [('sh_sla_policy_ids', 'in', self.ids)], limit=None)
            record.sla_ticket_count = len(tickets.ids)
    
    
    def action_view_tickets(self):
        self.ensure_one()
        tickets = self.env['sh.helpdesk.ticket'].sudo().search(
            [('sh_sla_policy_ids', 'in', self.ids)])
        action = self.env["ir.actions.actions"]._for_xml_id(
            "sh_all_in_one_helpdesk.sh_helpdesk_ticket_action")
        if len(tickets) > 1:
            action['domain'] = [('id', 'in', tickets.ids)]
        elif len(tickets) == 1:
            form_view = [
                (self.env.ref('sh_all_in_one_helpdesk.sh_helpdesk_ticket_form_view').id, 'form')]
            if 'views' in action:
                action['views'] = form_view + \
                    [(state, view)
                     for state, view in action['views'] if view != 'form']
            else:
                action['views'] = form_view
            action['res_id'] = tickets.id
        else:
            action = {'type': 'ir.actions.act_window_close'}
        return action