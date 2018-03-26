# -*- coding: utf-8 -*-
# © 2018 Rodrigo Colombo Vlaeminch (rodrigo.covl@gmail.com).

from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError


class ProductTemplate(models.Model):
    _inherit = "product.template"

    @api.depends('is_vehicle')
    def _compute_standard_price(self):
        super(ProductTemplate, self)._compute_standard_price()
        if self.is_vehicle:
            self.standard_price = self.env['fleet.vehicle'].search([('product_id', '=', self.id)]).car_value
