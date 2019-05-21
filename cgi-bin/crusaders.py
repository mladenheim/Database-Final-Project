#!/usr/bin/env python 

import cgi, cgitb
import mysql.connector
from mysql.connector import errorcode


cnx = mysql.connector.connect(user='mladenhe', password='qwerty', host='localhost', database='mladenhe1')

cursor = cnx.cursor()

try:
  cnx = mysql.connector.connect(user='mladenhe', password='qwerty', host='localhost', database='mladenhe1')
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)

else:
  cnx.close()
  #import cgi, cgitb
#import mysql.connector

#cnx = mysql.connector.connect(user='mladenheim', password='qwerty', host='localhost', database='mladenhe1')

#cnx.autocommit = True

#cursor = cnx.cursor()

form = cgi.FieldStorage()
 
query = 'select * from players, plays_for, teams where players.player_id = plays_for.player_id and plays_for.team_id = teams.team_id and teams.team_id = "40000";'

# html to connect with the data                                           
print ("Content-type:text/html\r\n\r\n")
print ('<html>')
print ('<head>')
print ('<title>Hello - Second CGI Program</title>')
print ('</head>')
print ('<body>')
cursor.execute(query)
for line in cursor:
    print('<p>' + line + '</p>')
print ('Heres the Crusaders!')
print ('</body>')
print ('</html>')
cursor.close()

cnx.close()

#print'<html>'
#print'<body>'
#print'HI'
#print'</body>'
#print'</html>'
