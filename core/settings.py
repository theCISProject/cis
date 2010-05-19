#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4 encoding=utf-8

import os, time

# this is the template that is used as the base for all
# rapidsms pages.  if you want to totally restyle your pages
# you should change this in your configuration .ini file
BASE_TEMPLATE = "layout.html"
# This is a similar concept, but for templating the login
# and logout screens
LOGIN_TEMPLATE = "core/login.html"
LOGGEDOUT_TEMPLATE = "core/loggedout.html"

RAPIDSMS_APPS = []