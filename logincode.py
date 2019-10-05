#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
import cgi,MySQLdb
f=cgi.FieldStorage()
userid=f.getvalue('userid')
password=f.getvalue('pass')
#print userid,"<br>"
#print password,"<br>"

con=MySQLdb.connect("127.0.0.1","root","","myproject",3306)
cur=con.cursor()
q="select * from tbl_login where userid=%s"
cur.execute(q,userid)
res=cur.fetchall()
status="true"
for r in res:
	status="false"
	if r[1]==password and r[2]=="true":
		print "<script>window.location.href='cookies.py?id=",userid,"';</script>"
	else:
		print "<script>alert('Login Details invalid');window.location.href='login.py';</script>"
if status=="true":
	query="select password from tbl_admin where adminid=%s"
	cur.execute(query,userid)
	res1=cur.fetchall()
	st="true"
	for r in res1:
		st="false"
		if r[0]==password:
			print "<script>window.location.href='admincookies.py?id=",userid,"';</script>"
		else:
			print "<script>alert('Login Details Invalid');window.location.href='login.py';</script>"
	if st=="true":
		print "<script>alert('Login Details Invalid');window.location.href='login.py';</script>"
	
	
	
	