# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "vzla_taxislr"
app_title = "ISLR Base Venezuela"
app_publisher = "Iron Graterol"
app_description = "Contiene la Base para el Calculo del ISLR en Documentos Fiscales"
app_icon = "octicon octicon-file-directory"
app_color = "'yellow'"
app_email = "ironxp@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/vzla_taxislr/css/vzla_taxislr.css"
# app_include_js = "/assets/vzla_taxislr/js/vzla_taxislr.js"

# include js, css files in header of web template
# web_include_css = "/assets/vzla_taxislr/css/vzla_taxislr.css"
# web_include_js = "/assets/vzla_taxislr/js/vzla_taxislr.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "vzla_taxislr.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "vzla_taxislr.install.before_install"
# after_install = "vzla_taxislr.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "vzla_taxislr.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"vzla_taxislr.tasks.all"
# 	],
# 	"daily": [
# 		"vzla_taxislr.tasks.daily"
# 	],
# 	"hourly": [
# 		"vzla_taxislr.tasks.hourly"
# 	],
# 	"weekly": [
# 		"vzla_taxislr.tasks.weekly"
# 	]
# 	"monthly": [
# 		"vzla_taxislr.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "vzla_taxislr.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "vzla_taxislr.event.get_events"
# }

