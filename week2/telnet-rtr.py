#!/usr/bin/env python
import time
import telnetlib

hostname = "184.105.247.70"

username = 'pyclass'

password = '88newclass'

PORT = 23

TIMEOUT = 6


def sendcmd(remote_conn, command):

    output = ""
    for i in command:
        remote_conn.write(str(i) + '\n')
        time.sleep(1)
        output += remote_conn.read_very_eager()
        
    return output
    
remote_conn = telnetlib.Telnet(hostname, PORT, TIMEOUT)

output = remote_conn.read_until('sername:', TIMEOUT)
remote_conn.write(username + '\n')

output = remote_conn.read_until('assword:', TIMEOUT)
remote_conn.write(password + '\n')

time.sleep(1)
command = [ "terminal length 0", "show ip int br" ]

output = sendcmd(remote_conn, command)

print output
