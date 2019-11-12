# -*- coding: utf-8 -*-
{
    'name': "Event Site visit report",

    'summary': """
        Dynamic Event Site visit report""",

    'description': """
        Sales Event Site visit report
    """,

    'author': "Daniel Winga",
    'website': "https://serp.com",


    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'event', 'event_modification'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/views.xml',
        # 'views/templates.xml',
        'wizards/eventsitevisit.xml',
        'reports/eventsitevisit.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}