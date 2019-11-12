# -*- coding: utf-8 -*-
# © 2013 Nicolas Bessi (Camptocamp SA)
# © 2014 Agile Business Group (<http://www.agilebg.com>)
# © 2015 Grupo ESOC (<http://www.grupoesoc.es>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': ' event products',
    'summary': "Add products to be available for site visit",
    'version': '11.0.1.0.1',
    'author': "Dan Winga, "
              "Khan Faisal, "
              "Daniel winga",
    'license': "AGPL-3",
    'maintainer': 'Daniel Winga',
    'category': 'Extra Tools',
    'website': 'www.serp.com',
    'depends': ['base_setup', 'event'],
    'data': [
        'views/event_product.xml',
        'views/extra_attendee.xml',


    ],
    'auto_install': False,
    'installable': True,
}
