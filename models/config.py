# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Config(models.Model):
    _name = 'hr_delegation.config'
    _description = 'HR Delegation: Config'

    name = fields.Char(string='Name')