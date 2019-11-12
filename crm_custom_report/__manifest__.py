# -*- coding: utf-8 -*-
{
    'name': "Sales pipeline/ Opportunity Report",

    'summary': """
        Dynamic Sales Person pipeline report""",

    'description': """
        Sales person pipeline report per period
        Sales person Leads report per period
    """,

    'author': "Daniel Winga",
    'website': "https://serp.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'crm'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/views.xml',
        # 'views/templates.xml',
        'wizards/salesleads.xml',
        'reports/salesleads.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}