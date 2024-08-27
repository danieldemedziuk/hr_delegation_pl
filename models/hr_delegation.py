# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Delegation(models.Model):
    _name = 'hr_delegation'
    _description = 'HR Delegation'

    name = fields.Char()
    date_start = fields.Datetime(string='Date start')
    date_end = fields.Datetime(string='Date end')
    project_id = fields.Many2one('project.project', string='Project')
    employee_id = fields.Many2one('hr.employee', string='Employee')

