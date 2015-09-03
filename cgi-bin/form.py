#!/usr/local/bin/python2.7
# -*- coding: UTF-8 -*-

import cgi

form = cgi.FieldStorage()
text1 = form.getfirst("TEXT_1", "нет данных")
text2 = form.getfirst("TEXT_2", "нет данных")


print ("Content-type: text/html\n" )
print( """<!DOCTYPE HTML>
        <html>
        <head>
            <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
            <title>Обработка данных форм</title>
        </head>
        <body>""" )

print ("<h2>Обработка данных форм</h2>" )
print ('TEXT_1: ', text1, '<br>')
print ('TEXT_2: ', text2)

print ("""</body>
        </html>""" )
