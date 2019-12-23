# -*- coding: utf-8 -*-
from datetime import time

from odoo import models
from odoo import api, fields, models, _


class AccUnReport(models.Model):
    _inherit = 'bank.statement.unreconciled'

    def print_bank_unreconciled(self):
        return self.env.ref('accounting_reports_bank_reconciliation.action_report_bank_unreconciled').report_action(self)