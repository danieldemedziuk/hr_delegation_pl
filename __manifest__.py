# -*- coding: utf-8 -*-
{
    'name': "HR Delegation PL",
    'version': '17.0.1.0.1',
    'category': 'Human Resources',
    'summary': "Polish business delegations of your company's employees.",
    'description': """
Polish business delegations of your company's employees.
    """,
    'author': "Daniel Demedziuk",
    'maintainer': 'Daniel Demedziuk',

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list

    'depends': [
        'base',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/config_data.xml',
        'views/hr_delegation_views.xml',
        'views/config_views.xml',
    ],

    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': True,
}
