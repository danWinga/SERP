# -*- coding: utf-8 -*-
# © 2013 Nicolas Bessi (Camptocamp SA)
# © 2014 Agile Business Group (<http://www.agilebg.com>)
# © 2015 Grupo ESOC (<http://www.grupoesoc.es>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Activity Feedback',
    'summary': "Adds activity feed back to calendar activity / daily work/ meeting",
    'version': '11.0.1.0.1',
    'author': "Daniel Winga, "
              "Khan Faisal, "
              "Daniel winga",
    'license': "AGPL-3",
    'maintainer': 'Daniel Winga',
    'category': 'Extra Tools',
    'website': 'www.serp.com',
    'depends': ['base_setup', 'calendar'],
    'data': [

        'views/calendar_feedback.xml',

    ],
    'auto_install': False,
    'installable': True,
}
