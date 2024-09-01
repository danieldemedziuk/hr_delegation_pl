# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Config(models.Model):
    _name = 'hr_delegation_pl.config'
    _description = 'HR Delegation: Config'

    name = fields.Char(string='Name')
    base_currency_id = fields.Many2one('res.currency', default=17)
    accommodation_rate = fields.Monetary(string='Accommodation rate', currency_field='base_currency_id')
    fare_rate = fields.Monetary(string='Fare rate', currency_field='base_currency_id')
    vehicle_low_capacity = fields.Monetary(string='Low capacity', currency_field='base_currency_id')
    vehicle_high_capacity = fields.Monetary(string='High capacity', currency_field='base_currency_id')
    motorbike_rate = fields.Monetary(string='Motorbike rate', currency_field='base_currency_id')
    moped_rate = fields.Monetary(string='Moped rate', currency_field='base_currency_id')
    international_rate_ids = fields.One2many('hr_delegation_pl.international_rates', 'config_id')


class InternationRates(models.Model):
    _name = 'hr_delegation_pl.international_rates'
    _description = 'HR Delegation: Config internation rates'
    _order = 'country_code asc'

    country_id = fields.Many2one('res.country', string='Country', required=True)
    country_code = fields.Char(string='Country code', related='country_id.code')
    currency_id = fields.Many2one('res.currency', string='Currency', required=True)
    config_id = fields.Many2one('hr_delegation_pl.config')
    base_currency_id = fields.Many2one('res.currency', related='config_id.base_currency_id')
    diet_value = fields.Monetary(string='Value', currency_field='base_currency_id')

