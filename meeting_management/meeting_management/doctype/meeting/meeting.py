# -*- coding: utf-8 -*-
# Copyright (c) 2021, Ruturaj Patil and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document

class Meeting(Document):
	def validate(self):
		"""Set missing names and warn if duplicate"""
		found=[]
		for attendee in self.attendees:
			if not attendee.full_name:
				attendee.full_name=get_full_name(attendee.attendee)
			
			if attendee.attendee in found:
				frappe.throw(_("Attendee {0} entered twice").format(attendee.attendee))
			
			found.append(attendee.attendee)


#white Listed Methods
@frappe.whitelist()
def get_full_name(attendee):
	user=frappe.get_doc("User",attendee)

	# the below code is concate the firstname, middleName, LastName 
	return " ".join(filter(None,[user.first_name,user.middle_name,user.last_name]))



# @frappe.whitelist()
# def get_meetings(start, end):
#     if not frappe.has_permission("Meeting","read"):
#         raise frappe.PermissionErorr
    
#     return frappe.db.sql(""" select 
#             timestamp(`date`,from_time) as start,
#             timestamp(`date`,to_time) as end,
#             name,
#             title,
#             status,
#             0 as all_day
#             from `tabMeeting`
#             where `date` between %(start)s and %(end)s""",{
#                 "start":start,
#                 "end":end
#             }, as_dict=True)
