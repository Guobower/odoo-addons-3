# -*- coding: utf-8 -*-
# © 2018 Rodrigo Colombo Vlaeminch (rodrigo.covl@gmail.com).

from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError


class FleetVehicle(models.Model):
    _inherit = 'fleet.vehicle'

    car_value = fields.Float (readonly = True)
    type_sale_price = fields.Selection([('percent', _('Percent')),
                                        ('fix_price', _('Fix price')),
                                        ('benefit_amount', _('Benefit amount'))],
                                       string='Benefit Type',
                                       default='percent', required=True,
                                       help=_("""Method for calculating the sale price of the vehicle:
                                                  *Percentage: A profit percentage is added to the cost of the vehicle.
                                                  *Fixed Price: Manually set price.
                                                  *Benefit value: Value added to cost."""))
    amount_price = fields.Float(default=0, required=True)

    @api.multi
    def write(self, vals):
        for record in self:
            ch_price = False
            car_value = record.car_value
            type_sale_price = record.type_sale_price
            amount_price = record.amount_price
            if 'car_value' in vals and record.car_value != vals['car_value']:
                ch_price, car_value = True, vals['car_value']
            if 'type_sale_price' in vals and record.type_sale_price != vals['type_sale_price']:
                ch_price, type_sale_price = True, vals['type_sale_price']
            if 'amount_price' in vals and record.amount_price != vals['amount_price']:
                ch_price, amount_price = True, vals['amount_price']
            if ch_price:
                if type_sale_price == 'percent':
                    price = car_value + ((car_value * amount_price) / 100)
                elif type_sale_price == 'fix_price':
                    price = amount_price
                elif type_sale_price == 'benefit_amount':
                    price = car_value + amount_price
                record.product_id.lst_price = record.product_id.list_price = price
        res = super(FleetVehicle, self).write(vals)
        return res

class FleetVehicleCost(models.Model):
    _inherit = 'fleet.vehicle.cost'

    @api.model
    def create(self, data):
        vehicle = False
        if 'vehicle_id' in data.keys():
            vehicle = self.env['fleet.vehicle'].browse(data['vehicle_id'])
        if vehicle and 'amount' in data.keys():
            vehicle.car_value = vehicle.car_value + (data['amount'] or 0.0)
        return super(FleetVehicleCost, self).create(data)

    @api.multi
    def write(self, vals):
        for record in self:
            ch_amount = False
            amount = record.amount
            vehicle_id = record.vehicle_id.id
            if 'amount' in vals and record.amount != vals['amount']:
                amount, ch_amount = vals['amount'], True
            if 'vehicle_id' in vals and record.vehicle_id.id != vals['vehicle_id']:
                vehicle_id, ch_amount = vals['vehicle_id'], True
            if ch_amount:
                record.vehicle_id.car_value = record.vehicle_id.car_value - record.amount
                vehicle = self.env['fleet.vehicle'].browse(vehicle_id)
                vehicle.car_value = vehicle.car_value + amount
        return super(FleetVehicleCost, self).write(vals)