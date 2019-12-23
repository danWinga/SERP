# -*- coding: utf-8 -*-
##############################################################################
#

#
#    It is forbidden to publish, distribute, sublicense, or sell copies
#    of the Software or modified copies of the Software.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    GENERAL PUBLIC LICENSE (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'bank Reconciliation Report',
    'version': '11.0.1',
    'author': 'Winga',
    'summary': 'Print a particular Bank Reconciliation report',
    'description': """  """,
    'category': 'Accounting',
    'website': 'https://www.serp.com/',
    'license': 'AGPL-3',

    'depends': ['base', 'account', 'bank_reconciliation',
                ],

    'data': [
        'views/report_bank_reconciliation.xml',
        'views/report_bank_unreconciled.xml',
    ],

    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
