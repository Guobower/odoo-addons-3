# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from __builtin__ import super

from odoo import api, models, fields, tools, exceptions
import datetime


class CashBox(models.Model):
    _name = 'cash.box'

    @api.model
    def _default_currency(self):
        return self.env.user.company_id.currency_id

    @api.multi
    def _flow_count(self):
        for record in self:
            record.flow_count = len(record.flow_ids)

    @api.multi
    def _actual_amount(self):
        for record in self:
            record.actual_amount = sum(map(lambda x: x.amount, record.flow_ids))

    name = fields.Char(string='Box', required=True)
    description = fields.Text(string='Description')
    flow_ids = fields.One2many('cash.flow', 'cash_box_id', string='Cash flow')
    currency_id = fields.Many2one(comodel_name='res.currency', default=_default_currency)
    active = fields.Boolean(string='Active', default=True)
    flow_count = fields.Integer(string='Flows', readonly=True, compute='_flow_count')
    color = fields.Integer(string='Color Index')
    actual_amount = fields.Float(string="Actual amount", readonly=True, compute='_actual_amount')

    @api.multi
    def toggle_active(self):
        for record in self:
            super(CashBox, record).toggle_active()


class CashFlow(models.Model):
    _name = 'cash.flow'
    _inherit = ['mail.thread']
    _order = "date_flow desc"

    #TODO: track events related to the document.

    name = fields.Char(string='Concept', required=True, track_visibility='always')
    currency_id = fields.Many2one('res.currency', related='cash_box_id.currency_id', store=True, related_sudo=False)
    amount = fields.Monetary(string='Money', required=True, currency_field='currency_id', track_visibility='always')
    cash_box_id = fields.Many2one(string='Cash Box', comodel_name='cash.box', required=True)
    note = fields.Text(string='Extra note')
    date_flow = fields.Datetime(string='Date', required=True, default=datetime.datetime.now(), track_visibility='always')

    @api.model
    def create(self, vals):
        return super(CashFlow, self.with_context(mail_create_nolog=True)).create(vals)

    @api.multi
    def write(self, vals):
        return super(CashFlow, self.with_context(mail_create_nolog=True)).write(vals)