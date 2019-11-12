# -*- coding: utf-8 -*-
# © 2013 Nicolas Bessi (Camptocamp SA)
# © 2014 Agile Business Group (<http://www.agilebg.com>)
# © 2015 Grupo ESOC (<http://www.grupoesoc.es>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Partner first, second name and last name',
    'summary': "Split first name, middle name and last name for non company partners",
    'version': '11.0.1.0.1',
    'author': "Camptocamp, "
              "Grupo ESOC Ingeniería de Servicios, "
              "Tecnativa, "
              "LasLabs, "
              "Khan Faisal, "
              "Daniel winga",
    'license': "AGPL-3",
    'maintainer': 'Camptocamp, Acsone',
    'category': 'Extra Tools',
    'website': 'h',
    'depends': ['base_setup'],
    'post_init_hook': 'post_init_hook',
    'data': [
        'views/base_config_view.xml',
        'views/res_partner.xml',
        'views/res_user.xml',

    ],
    'auto_install': False,
    'installable': True,
}
