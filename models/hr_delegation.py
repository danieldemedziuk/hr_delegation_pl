# -*- coding: utf-8 -*-
from datetime import datetime

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class Delegation(models.Model):
    _name = 'hr_delegation_pl'
    _description = 'HR Delegation'

    name = fields.Char(string='Delegation number', required=True, readonly=True, default=lambda self: _('New'))
    date_start = fields.Datetime(string='Date start', required=True)
    date_end = fields.Datetime(string='Date end', required=True)
    project_id = fields.Many2one('project.project', string='Project')
    employee_id = fields.Many2one('hr.employee', string='Employee', required=True)
    state = fields.Selection([('draft', 'Draft'), ('new', 'New'), ('in-progress', 'In progress'), ('done', 'Done'), ('cancel', 'Canceled')], string='State', default='draft')
    note = fields.Html(string='Note')
    vehicle_id = fields.Many2one('fleet.vehicle', string='Company vehicle')
    private_vehicle_id = fields.Many2one('hr_delegation_pl.private_vehicle', string='Private vehicle')
    need_hotel = fields.Boolean(string='Need hotel')
    daily_returns = fields.Boolean(string='Need hotel')

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('delegation.sequence') or _('New')
        vals['state'] = 'new'
        res = super(Delegation, self).create(vals)

        return res

    @api.constrains('date_start', 'date_end')
    def _check_correct_dates(self):
        if self.date_end < self.date_start:
            raise ValidationError(_("The end date must be greater than the start date."))

    def action_settle(self):
        self.state = 'in-progress'

    def action_done(self):
        self.state = 'done'

    def action_cancel(self):
        self.state = 'cancel'


class PrivateVehicle(models.Model):
    _name = 'hr_delegation_pl.private_vehicle'
    _description = 'HR Delegation: Private vehicle'

    name = fields.Char(string='Name', default='NEW', required=True, readonly=True)
    brand_id = fields.Many2one('fleet.vehicle.model.brand', string='Brand')
    model_id = fields.Char(string='Model')
    license_plate = fields.Char(string='License plate', required=True)
    engine_capacity = fields.Float(string='Engine capacity', required=True)

    @api.model
    def create(self, vals):
        vals['name'] = f"{self.env['fleet.vehicle.model.brand'].browse(vals['brand_id']).name} {vals['model_id']} / {vals['license_plate']}"
        res = super(PrivateVehicle, self).create(vals)

        return res

