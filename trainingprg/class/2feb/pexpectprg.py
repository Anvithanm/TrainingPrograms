import pexpect
import sys
import getpass
mail=pexpect.spawn('python gmailprg2.py')
mail.logfile_read = sys.stdout
mail.expect('Username:')
mail.sendline('anvithanm22@gmail.com')
mail.expect('Password')
password=getpass.getpass()
mail.sendline(password)
mail.expect('to')
mail.sendline('anvithah2016@gmail.com')
mail.expect('sub')
mail.sendline('test2')
mail.expect('line')
mail.sendline('email analysis2')
mail.expect('has been sent to')
mail.sendline('test2'+'anvithah2016@gmail.com')
mail.close()
