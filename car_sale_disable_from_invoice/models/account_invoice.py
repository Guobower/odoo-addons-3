# -*- coding: utf-8 -*-

from odoo import models, api

class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    def vehicle_toggle_active(self):
        v_ids = []
        for line in self.invoice_line_ids:
            if line.product_id and line.product_id.is_vehicle:
                v_ids.append(line.product_id.vehicle_id.id)
        vehicle_ids = self.env['fleet.vehicle'].browse(v_ids)
        for v in vehicle_ids:
            v.toggle_active()

    @api.multi
    def action_invoice_open(self):
        res = super(AccountInvoice, self).action_invoice_open()
        self.vehicle_toggle_active()
        return res

    @api.multi
    def action_invoice_cancel(self):
        res = super(AccountInvoice, self).action_invoice_cancel()
        self.vehicle_toggle_active()
        return res
