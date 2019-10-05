#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
import cgi,MySQLdb
f=cgi.FieldStorage()
username=f.getvalue('username')
gender=f.getvalue('gender')
mobileno=f.getvalue('mobileno')
email=f.getvalue('email')
enquiry=f.getvalue('enquiry')
#print username,"<br>"
#print gender,"<br>"
#print mobileno,"<br>"
#print email,"<br>"
#print enquiry,"<br>"
con=MySQLdb.connect("127.0.0.1","root","","myproject",3306)
cur=con.cursor()
q="insert into tbl_enquiry(name,gender,mobileno,email,enquiry_text,enquiry_date) values(%s,%s,%s,%s,%s,sysdate())";
v=username,gender,mobileno,email,enquiry
cur.execute(q,v)
con.commit()
con.close()
print "<script>alert('Enquiry successfull submitted');window.location.href='enquiry.py'</script>"







