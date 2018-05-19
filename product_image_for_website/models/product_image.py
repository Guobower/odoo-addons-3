# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import api, models, fields, tools, exceptions


class ProductImage(models.Model):
    _inherit = 'product.image'

    @api.multi
    def init(self):
        for record in self.search([]):
            record.image = tools.image.image_resize_image(record.image, size=(640, 480))

    @api.model
    def create(self, vals):
        if 'image' in vals.keys():
            try:
                vals['image'] = tools.image.image_resize_image(vals['image'], size=(640, 480))
            except Exception:
                pass
        return super(ProductImage, self).create(vals)

    @api.multi
    def write(self, vals):
        if 'image' in vals.keys():
            try:
                vals['image'] = tools.image.image_resize_image(vals['image'], size=(640, 480))
            except Exception:
                pass
        return super(ProductImage, self).write(vals)
