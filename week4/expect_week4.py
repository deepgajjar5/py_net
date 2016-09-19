import pexpect 

username = 'pyclass'
ip = '184.105.247.71'
passwd = '88newclass'

conn = pexpect.spawn('ssh -l {} {}'.format(username, ip))

conn.expect('ssword:')
conn.sendline(passwd)

conn.expect('#')
conn.sendline('config t')

conn.expect('#')
conn.sendline('logging buffered 23000')

conn.expect('#')
conn.sendline('exit')

conn.expect('#')
conn.sendline('show run')

conn.expect('#')
print(conn.before)
