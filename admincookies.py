#!C:\Python27\python.exe

import cgi
import Cookie

c=Cookie.SimpleCookie()

c['aid']=cgi.FieldStorage().getvalue('id').strip(' ')
c['aid']['expires']=3*60*60
print c['aid']

print "Content-Type:text/html\n\n"
print "<script>window.location.href='adminzone/adminwelcome.py';</script>"