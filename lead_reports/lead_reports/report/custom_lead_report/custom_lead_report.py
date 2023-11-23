# # Copyright (c) 2023, Ameer Muavia Shah and contributors
# # For license information, please see license.txt

import frappe
from frappe import _


def execute(filters=None):
    columns = get_columns()
    data = []

    # Validate and setup filters
    from_date, to_date = filters.get("from_date"), filters.get("to_date")

    filters_for_leads = {
        "company": filters.get("company"),
        "creation": ["between", [from_date, to_date]]
    }

    # Fetch leads data
    leads_data = frappe.get_all("Lead",
                                filters=filters_for_leads,
                                fields=["name", "lead_name","status", "email_id", "mobile_no",
                                        "custom_lead_update", "source",
                                        "date(creation) as creation_date", "lead_owner"])

    # Prepare data for report
    for lead in leads_data:
        data.append({
            "name": lead.name,
            "creation_date": lead.creation_date,
            "lead_name": lead.lead_name,  # Assuming 'status' is the lead name, adjust as needed
            "email_id": lead.email_id,
            "mobile_no": lead.mobile_no,
            "source": lead.source,
            "status": lead.status,
            "custom_lead_update": lead.custom_lead_update,
            "lead_owner": lead.lead_owner
        })

    # Generate chart data
    chart = get_chart_data(leads_data, filters, filters_for_leads)

    return columns, data, None, chart


def get_columns():
    return [
        {
            "label": _("ID"),
            "fieldname": "name",
            "fieldtype": "Data",
            "width": 200
        },
        {
            "label": _("Creation Date"),
            "fieldname": "creation_date",
            "fieldtype": "Data",
            "width": 150
        },
        {
            "label": _("Full Name"),
            "fieldname": "lead_name",
            "fieldtype": "Data",
            "width": 200
        },
        {
            "label": _("Email"),
            "fieldname": "email_id",
            "fieldtype": "Data",
            "width": 200
        },
        {
            "label": _("Phone"),
            "fieldname": "mobile_no",
            "fieldtype": "Data",
            "width": 200
        },
        {
            "label": _("Source"),
            "fieldname": "source",
            "fieldtype": "Data",
            "width": 200
        },
        {
            "label": _("Status"),
            "fieldname": "status",
            "fieldtype": "Data",
            "width": 200
        },
        {
            "label": _("Lead Update"),
            "fieldname": "custom_lead_update",
            "fieldtype": "Data",
            "width": 200
        },
        {
            "label": _("Lead Owner"),
            "fieldname": "lead_owner",
            "fieldtype": "Data",
            "width": 200
        },]


def get_chart_data(leads_data, filters, filters_for_leads):
    group_by = filters.get("type", "status").lower()
    count_data = frappe.get_all("Lead",
                                filters=filters_for_leads,
                                fields=[f"{group_by} as label",
                                        "count(name) as lead_count"],
                                group_by=group_by)

    chart = {
        "data": {
            "labels": [x["label"] for x in count_data],
            "datasets": [{
                "name": "Lead Count",
                "values": [x["lead_count"] for x in count_data]
            }]
        },
        "type": "bar"
    }

    return chart
