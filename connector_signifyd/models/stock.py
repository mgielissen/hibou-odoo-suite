from odoo import fields, models


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    singifyd_case_id = fields.Many2one(related='sale_id.signifyd_case_id')
    signifyd_hold = fields.Selection(related='sale_id.signifyd_disposition_status')

    def action_view_signifyd_case(self):
        self.ensure_one()
        form_id = self.env.ref('gcl_signifyd_connector.signifyd_case_form_view').id
        context = {'create': False, 'delete': False, 'id': self.sale_id.signifyd_case_id.id}
        return {
            'type': 'ir.actions.act_window',
            'name': 'Signifyd Case',
            'view_mode': 'form',
            'views': [(form_id, 'form')],
            'res_model': 'signifyd.case',
            'res_id': self.singifyd_case_id.id,
            'context': context,
        }