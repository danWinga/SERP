# -*- coding: utf-8 -*-

from datetime import datetime, timedelta

from odoo import models, fields, api
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT as DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT as DATETIME_FORMAT


class SalesWorkReportWizard(models.TransientModel):
    _name = 'event.site.visit.report.wizard'

    start_date = fields.Date(string="Start Date", required=True, default=fields.Date.today)
    end_date = fields.Date(string="End Date", required=True, default=fields.Date.today)
    event_ids = fields.Many2many('event.event', string="Site visit")

    @api.multi
    def get_report(self):
        """Call when button 'Get Report' clicked.
        """
        event_attendees = self.env['event.registration'].search([])
        groupby_dict = {}
        for event in self.event_ids:
            filtered_events = list(filter(lambda x: x.event_id == event, event_attendees))
            filtered_by_date = list(
                filter(lambda x: x.date_open >= self.start_date and x.date_open <= self.end_date, filtered_events))
            groupby_dict[event.name] = filtered_by_date

        final_dict = {}
        for event in groupby_dict.keys():

            temp = []

            for attendee in groupby_dict[event]:

                temp_2 = []
                temp_2.append(attendee.name)
                temp_2.append(attendee.date_open)
                temp_2.append(attendee.project_id.name)
                temp_2.append(attendee.date_closed)
                temp_2.append(attendee.phone)
                temp_2.append(attendee.email)
                temp_2.append(attendee.attendee_type)
                temp_2.append(attendee.extraNumber)
                temp_2.append(attendee.salesperson_id.name)

                temp_2.append(attendee.state)
                temp.append(temp_2)
            final_dict[event] = temp
        data = {
            'ids': self,
            'model': self._name,
            'form': final_dict,
            'start_date': self.start_date,
            'end_date': self.end_date,
        }

        # use `module_name.report_id` as reference.
        # `report_action()` will call `get_report_values()` and pass `data` automatically.
        return self.env.ref('event_site_visit_report.site_visit_report').report_action(self, data=data)


class ReportSalesWork(models.AbstractModel):
    """Abstract Model for report template.

    for `_name` model, please use `report.` as prefix then add `module_name.report_name`.
    """

    _name = 'report.event_site_visit_report.event_site_visit_report_view'

    @api.model
    def get_report_values(self, docids, data=None):

        return {
            'doc_ids': data.get('ids'),
            'doc_model': data.get('model'),
            'data': data['form'],
            'start_date': data['start_date'],
            'end_date': data['end_date'],

        }
