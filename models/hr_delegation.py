# -*- coding: utf-8 -*-
from datetime import datetime

from odoo import models, fields, api


class Delegation(models.Model):
    _name = 'hr_delegation_pl'
    _description = 'HR Delegation'

    def compute_name(self):
        last_num = self.env['hr_delegation_pl'].search([], limit=1, order='id desc')

        if last_num:
            pass
        else:
            self.name = f'DG/{datetime.today().year}/0001'

    name = fields.Char(string='Delegation number', default=compute_name)
    date_start = fields.Datetime(string='Date start', required=True)
    date_end = fields.Datetime(string='Date end', required=True)
    project_id = fields.Many2one('project.project', string='Project')
    employee_id = fields.Many2one('hr.employee', string='Employee', required=True)
    state = fields.Selection([('new', 'New'), ('in-progress', 'In progress'), ('settle', 'Settle'), ('done', 'Done'), ('cancel', 'Canceled')],
                             string='State', default='new')
    note = fields.Html(string='Note')



