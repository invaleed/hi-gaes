#!/usr/bin/env python

# enable debugging
import cgitb
import platform

cgitb.enable()

print "Content-Type: text/plain;charset=utf-8"
print
print "Hi Gaes!\n"
print "Rendered on:", platform.uname()[1]
