// frappe.views.calendar["Meeting"]={
//     field_map:{
//         "start":"start",
//         "end":"end",
//         "id":"name",
//         "title":"title",
//         "status":"status"
//     },
//     get_events_method:"meeting_management.api.get_meetings"
// }

frappe.views.calendar["Meeting"] = {
    field_map: {
            "start": "start",
            "end": "end",
            "id": "name",
            "title": "title",
            "status": "status",
            "allDay": "all_day",
    },
    get_events_method: "meeting_management.api.get_meetings"
    // meeting_manager.meeting_manager.doctype.meeting.meeting.get_meetings
}
