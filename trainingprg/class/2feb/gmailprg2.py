import smtplib
import getpass
website='smtp.gmail.com'
port=587
server = smtplib.SMTP(website, port)
server.ehlo()
server.starttls()
server.ehlo()
username=raw_input("Username:")
password=getpass.getpass()
server.login(username, password)
#print "Hello "+username+"! \n You are connected with the "+website+"\nYou can send your mail\n"
#password=raw_input('enter your password : ');
to=raw_input("to");
sub=raw_input("sub");
#print "Enter the content. Your last line should be as 'end'"
#text="";
#while line != "end":
#text+=line+"\n";
line=raw_input("line")
message = 'Subject: %s\n\n%s' % (sub, line)
server.sendmail(username, to, message)
print sub+"has been sent to"+to

