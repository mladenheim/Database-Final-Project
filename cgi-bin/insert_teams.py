#!/usr/bin/env python3

import cgi, cgitb
import mysql.connector

cnx = mysql.connector.connect(user='mladenheim', password='qwerty', host ='localhost', database='mladenhe1')

cnx.autocommit = True

cursor = cnx.cursor(buffered=True)

form = cgi.FieldStorage()

# get data from feilds
IDnumber = form.getvalue('IDnumber')
teamName = form.getbalue('teamName')
teamCity = form.getvalue('teamCity')
values = (IDnumber, teamName, teamCity)

# example values = (12345, "Ballers', "Brooklyn")
query = "insert into teams values(%s, %s, %s);"

# html to connect with the data
print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Hello - Second CGI Program</title>")
print("</head>")
print("<body>")
cursor.execute(query, values)
print("The new team has been created!")
print("</body>")
print("</html>")
cursor.close()
cnx.close()
