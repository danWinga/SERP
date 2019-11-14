# Copyright 2019 ADHOC SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Cash Flow',
    'version': '12.0.1.1.0',
    'license': 'LGPL-3',
    'author': 'Dan winga, '
              'SERP',
    'website': '#',
    'depends': [
        'mis_builder',
    ],
    'data': [
        'security/mis_cash_flow_security.xml',
        'report/mis_cash_flow_views.xml',
        'views/mis_cash_flow_forecast_line_views.xml',
        'views/account_account_views.xml',
        'data/mis_report_style.xml',
        'data/mis_report.xml',
        'data/mis_report_instance.xml',
    ],
    'installable': True,
    'maintainers': ['jjscarafia'],
    'development_status': 'Beta',
}
