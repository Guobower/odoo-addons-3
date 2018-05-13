# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import api, models, fields, tools


class ProductImage(models.Model):
    _inherit = 'product.image'

    full_image = fields.Binary('Full Image', attachment=True, oldname='image')
    image = fields.Binary('Image', attachment=True, compute='_resize_image')

    @api.multi
    def init(self):
        for record in self.search([]):
            try:
                record.full_image = record.image
            except Exception:
                pass

    @api.multi
    def _resize_image(self):
        for record in self:
            try:
                record.image = tools.image.image_resize_image(record.full_image, size=(640, 480))
            except Exception:
                record.image = record.full_image
