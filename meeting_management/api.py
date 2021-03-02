import frappe
from frappe.utils import add_days,nowdate

@frappe.whitelist()
def send_invitation_emails(meeting):
    meeting=frappe.get_doc("Meeting",meeting)
    # meeting.check_permission("email")
    print("\n\n\n\n\n\n\n\n\n\n\n",meeting,"\n\n\n\n\n\n\n\n\n\n\n")

    if meeting.status=="Planned":
        frappe.sendmail(recipients=[d.attendee for d in meeting.attendees],
                        sender=frappe.session.user, 
                        subject=meeting.title, 
                        message=meeting.invitation_message,
                        reference_doctype=meeting.doctype,
                        reference_name=meeting.name
		)

        meeting.status="Invitation Sent"
        meeting.save()
        frappe.msgprint("Invitaion Sent")
    else:
        frappe.msgprint("Meeting Status Must be 'Planned'")

@frappe.whitelist()
def get_meetings(start, end):
    if not frappe.has_permission("Meeting","read"):
        raise frappe.PermissionErorr

    ss=frappe.db.sql(""" select 
            timestamp(`date`,from_time) as start,
            timestamp(`date`,to_time) as end,
            name,
            title,
            status,
            0 as all_day
            from `tabMeeting`
            where `date` between %(start)s and %(end)s""",{
                "start":start,
                "end":end
            })
    print("\n\n\n\n\n\n\n\n\n\n",ss,"\n\n\n\n\n\n\n\n")
    
    return frappe.db.sql(""" select 
            timestamp(`date`,from_time) as start,
            timestamp(`date`,to_time) as end,
            name,
            title,
            status,
            0 as all_day
            from `tabMeeting`
            where `date` between %(start)s and %(end)s""",{
                "start":start,
                "end":end
            },as_dict=True)

@frappe.whitelist()
def make_orientation_meeting(doc, method):
    """ Create Orientation Meeting When a new User is created """
    meeting=frappe.get_doc({
        "doctype":"Meeting",
        "title":"Orientation Meeting for {0}".format(doc.first_name),
        "date":add_days(nowdate(),1), 
        "from_time":"10:00",
        "to_time":"10:30",
        "status":"Planned",
        "attendees":[{
            "attendee":doc.name
        }]
    })
    meeting.flags.ignore_permission=True
    meeting.insert()