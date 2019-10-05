#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
import cgi,MySQLdb
f=cgi.FieldStorage()
username=f.getvalue('username')
dob=f.getvalue('dob')
gender=f.getvalue('gender')
mobileno=f.getvalue('mobileno')
email=f.getvalue('email')
qualification=f.getvalue('qualification')
address=f.getvalue('address')
password=f.getvalue('pass')
cpass=f.getvalue('cpass')
#print username,"<br>"
#print dob,"<br>"
#print gender,"<br>"
#print mobileno,"<br>"
#print email,"<br>"
#print qualification,"<br>"
#print address,"<br>"
#print password,"<br>"
#print cpass,"<br>"
con=MySQLdb.connect("127.0.0.1","root","","myproject",3306)
cur=con.cursor()
q1="insert into tbl_registration values(%s,%s,%s,%s,%s,%s,%s,sysdate())"
v1=username,dob,gender,mobileno,email,qualification,address
cur.execute(q1,v1)
q2="insert into tbl_login values(%s,%s,'true')"
v2=email,password
cur.execute(q2,v2)
con.commit()
con.close()
print "<script>alert('Registration successfull submitted');window.location.href='reg.py'</script>"






