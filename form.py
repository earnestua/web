#!/usr/local/bin/python2.7
# -*- coding: UTF-8 -*-

import cgi

form = cgi.FieldStorage()
text1 = form.getfirst("TEXT_1", "не задано")
text2 = form.getfirst("TEXT_2", "не задано")

print "Content-type: text/html\n" 
print """<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Обработка данных форм</title>
        </head>
        <body>""" 

print text1
print text2

print """</body>
        </html>""" 
