# -*- coding: utf-8 -*-
from odoo import models,fields,api, _

class ReasonCancelation(models.TransientModel):
    _name ='reason.cancelation'
    _description = 'reason.cancelation'

    motivo_cancelacion = fields.Selection(
        selection=[('01', ('Comprobante emitido con errores con relación')),
                   ('02', ('Comprobante emitido con errores sin relación')),
                   ('03', ('No se llevó a cabo la operación')),
                   ('04', ('Operación nominativa relacionada en la factura global')),
                   ],
        string=('Motivo de cancelación'), 
    )

    foliosustitucion = fields.Char(string=_('Folio Sustitucion'))

    def Confirmar(self):
        if self.env.context.get('active_id') and self.env.context.get('active_model') == "hr.payslip":
            move_obj = self.env['hr.payslip'].browse(self.env.context['active_id'])
            ctx = {'motivo_cancelacion':self.motivo_cancelacion,'foliosustitucion':self.foliosustitucion or False}
            return move_obj.with_context(ctx).action_cfdi_cancel()

