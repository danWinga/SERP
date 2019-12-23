# -*- coding: utf-8 -*-
from datetime import time

from odoo import models
from odoo import api, fields, models, _


class AccMoveReport(models.Model):
    _inherit = 'bank.statement'

    def print_bank_reconciliation(self):
        return self.env.ref('accounting_reports_bank_reconciliation.action_report_bank_reconciliation').report_action(self)