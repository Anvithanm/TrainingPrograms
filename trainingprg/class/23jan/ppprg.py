import pexpect
m_p = pexpect.spawn('python product.py')
m_p.timeout=1200
m_p.expect ('gmail')
m_p.sendline('anvithanm22@gmail.com')
m_p.expect('Password:')
m_p.sendline('nmbsa-bubli1994')
m_p.expect('to')
m_p.sendline('shwarya777@gmail.com')
m_p.expect('sub')
m_p.sendline('email analysis')
m_p.close()
