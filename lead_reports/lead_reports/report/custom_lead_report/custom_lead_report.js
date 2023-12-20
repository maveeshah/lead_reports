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
  onload: function () {
    frappe.query_report._get_filters_html_for_print = frappe.query_report.get_filters_html_for_print;
    frappe.query_report.get_filters_html_for_print = print_settings => {
      const me = frappe.query_report,
        encode = svg => 'data:image/svg+xml;base64,' + btoa((new XMLSerializer()).serializeToString(svg));
      let applied_filters = me._get_filters_html_for_print();

      if (me.chart && me.chart.svg) {
        applied_filters += `<hr><img alt="${__('Chart')}" src="${encode(me.chart.svg)}" />`;
      }

      return applied_filters;

    };

  }
};
