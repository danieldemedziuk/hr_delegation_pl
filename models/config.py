# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Config(models.Model):
    _name = 'hr_delegation.config'
    _description = 'HR Delegation: Config'

    name = fields.Char(string='Name')
    accommodation_rate = fields.Monetary(string='Accommodation rate')
    fare_rate = fields.Monetary(string='Fare rate')
    vehicle_low_capacity = fields.Monetary(string='Low capacity')
    vehicle_high_capacity = fields.Monetary(string='High capacity')
    motorbike_rate = fields.Monetary(string='Motorbike rate')
    moped_rate = fields.Monetary(string='Moped rate')
    international_rate_ids = fields.One2many('hr_delegation.international_rates', 'config_id')


class InternationRates(models.Model):
    _name = 'hr_delegation.international_rates'
    _description = 'HR Delegation: Config internation rates'
    _order = 'country_code asc'

    country_id = fields.Many2one('res.country', string='Country')
    country_code = fields.Char(string='Country code', related='country_id.code')
    currency_id = fields.Many2one('res.currency', string='Currency')
    diet_value = fields.Monetary(string='Value')
    config_id = fields.Many2one('hr_delegation.config')
