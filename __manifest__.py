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
    'depends': [
        'project',
        'hr',
    ],
    'data': [
        'security/ir.model.access.csv',

        'data/config_data.xml',
        'data/sequence_data.xml',

        'views/hr_delegation_views.xml',
        'views/config_views.xml',
    ],

    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': True,
}
