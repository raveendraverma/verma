#!C:\Python27\python.exe

import Cookie
import cgi
import MySQLdb
c=Cookie.SimpleCookie()

c['userid']=cgi.FieldStorage().getvalue('id').strip(' ')
c['userid']['expires']=3*60*60
print c['userid']

con=MySQLdb.connect("127.0.0.1","root","","myproject",3306)
cur=con.cursor()
q="select name from tbl_registration where email=%s"
id=cgi.FieldStorage().getvalue('id').strip(' ')
cur.execute(q,id)
res=cur.fetchall()
username=""
for r in res:
	username=r[0]
c['pyname']=username
c['pyname']['expires']=3*60*60
print c['pyname']

print "Content-Type:text/html\n\n"
print "<script>window.location.href='userzone/welcome.py';</script>"





