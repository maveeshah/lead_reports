// Copyright (c) 2023, Ameer Muavia Shah and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Custom Lead Report"] = {
  filters: [
    {
      fieldname: "type",
      label: __("Type"),
      fieldtype: "Select",
      options: ["Status", "Source"],
      default: "Status",
    },
    {
      fieldname: "company",
      label: __("Company"),
      fieldtype: "Link",
      options: "Company",
      default: frappe.defaults.get_user_default("Company"),
    },
    {
      fieldname: "from_date",
      label: __("From Date"),
      fieldtype: "Date",
      default: frappe.datetime.get_today(),
    },
    {
      fieldname: "to_date",
      label: __("To Date"),
      fieldtype: "Date",
      default: frappe.datetime.get_today(),
    },
  ],
};
