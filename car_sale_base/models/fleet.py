# -*- coding: utf-8 -*-
# © 2018 Rodrigo Colombo Vlaeminch (rodrigo.covl@gmail.com).

from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError


class FleetVehicle(models.Model):
    _inherit = 'fleet.vehicle'

    product_id = fields.Many2one('product.template', 'Product',
                                 help='Product configure', ondelete='cascade',
                                 readonly=True)
    year = fields.Integer(string="Matriculation year")
    waranty = fields.Char(string="Waranty")
    extras = fields.Html(string="Extras")

    @api.model
    def create(self, data):
        vehicle = super(FleetVehicle, self.with_context(mail_create_nolog=True)).create(data)
        print vehicle.id
        product = self.env['product.template'].create({'name': vehicle.model_id.brand_id.name + ' ' + vehicle.model_id.name,
                                                       'standard_price': vehicle.car_value,
                                                       'type': 'consu',
                                                       'is_vehicle': True})
        vehicle.product_id = product.id
        product.write({'vehicle_id': vehicle.id})
        return vehicle

    @api.multi
    def unlink(self):
        for record in self:
            product_to_unlink = record.env['product.template'].search([['id', '=', record.product_id.id]])
            super(FleetVehicle, record).unlink()
            if not product_to_unlink.unlink():
                product_to_unlink.toggle_active()

    @api.multi
    def toggle_active(self):
        for record in self:
            record.product_id.toggle_active()
            super(FleetVehicle, record).toggle_active()