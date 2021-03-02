// Copyright (c) 2021, Ruturaj Patil and contributors
// For license information, please see license.txt
frappe.ui.form.on("Meeting",{
	send_emails: function(frm){
		if (frm.doc.status==="Planned"){
			frappe.call({
				method:"meeting_management.api.send_invitation_emails",
				args:{
					meeting:frm.doc.name
				}
			});
		}
		
	}
})


frappe.ui.form.on('Meeting Attendee', {
	attendee : function(frm,cdt,cdn){
		var attendee=frappe.model.get_doc(cdt,cdn)
		if(attendee.attendee){
			// if attendee is present then get full name
			frappe.call({
				method:"meeting_management.meeting_management.doctype.meeting.meeting.get_full_name",
				args:{
					attendee:attendee.attendee
				},
				callback:function(r){
					frappe.model.set_value(cdt,cdn,"full_name",r.message);
				}
			});
		}else{
			// If no attendee is present clear full name
			frappe.model.set_value(cdt,cdn,"full_name",null)
		}
	}
});
