# -*- coding: utf-8 -*-
# © 2018 Rodrigo Colombo Vlaeminch (rodrigo.covl@gmail.com).

from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    is_vehicle = fields.Boolean('Is a Vehicle', default=False)
    vehicle_id = fields.Many2one('fleet.vehicle', readonly=True, string="Vehicle")