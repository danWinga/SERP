# -*- coding: utf-8 -*-

from datetime import datetime, timedelta

from odoo import models, fields, api
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT as DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT as DATETIME_FORMAT


class LeadsSalesReportWizard(models.TransientModel):
    _name = 'leads.sales.report.wizard'  # pipeline.recap.report.wizard

    start_date = fields.Date(string="Start Date", required=True, default=fields.Date.today)
    end_date = fields.Date(string="End Date", required=True, default=fields.Date.today)
    user_ids = fields.Many2many('res.users', string="Salesperson")

    @api.multi
    def get_report(self):
        """Call when button 'Get Report' clicked.
        """
        crm_tasks = self.env['crm.lead'].search([])
        groupby_dict = {}
        for user in self.user_ids:
            filtered_tasks = list(filter(lambda x: x.user_id == user, crm_tasks))
            filtered_by_date = list(
                filter(lambda x: x.create_date >= self.start_date and x.create_date <= self.end_date, filtered_tasks))
            groupby_dict[user.name] = filtered_by_date

        final_dict = {}
        for user in groupby_dict.keys():
            temp = []
            for task in groupby_dict[user]:
                temp_2 = []
                temp_2.append(task.create_date)
                temp_2.append(task.name)
                temp_2.append(task.partner_address_name)
                temp_2.append(task.mobile)
                temp_2.append(task.product_id.name)
                temp_2.append(task.planned_revenue)
                temp_2.append(task.description)
                temp.append(temp_2)
            final_dict[user] = temp
        data = {
            'ids': self,
            'model': self._name,
            'form': final_dict,
            'start_date': self.start_date,
            'end_date': self.end_date,
        }

        # use `module_name.report_id` as reference.
        # `report_action()` will call `get_report_values()` and pass `data` automatically.
        return self.env.ref('crm_custom_report.leads_report').report_action(self, data=data)


class ReportLeadsSales(models.AbstractModel):
    """Abstract Model for report template.

    for `_name` model, please use `report.` as prefix then add `module_name.report_name`.
    """

    _name = 'report.crm_custom_report.leads_sales_report_view'

    @api.model
    def get_report_values(self, docids, data=None):

        return {
            'doc_ids': data.get('ids'),
            'doc_model': data.get('model'),
            'data': data['form'],
            'start_date': data['start_date'],
            'end_date': data['end_date'],

        }
