#!/usr/bin/env python3

import cgi
import cgitb
import math

# enable CGI traceback in case of errors
cgitb.enable()

# parse form data
form = cgi.FieldStorage()
a = float(form["a"].value)
b = float(form["b"].value)
c = float(form["c"].value)

# solve quadratic equation
discriminant = b**2 - 4*a*c
if discriminant < 0:
    roots = None
elif discriminant == 0:
    x = -b / (2*a)
    roots = (x,)
else:
    x1 = (-b + math.sqrt(discriminant)) / (
