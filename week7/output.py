from jsonrpclib import Server
import sys
import ssl
import re
ssl._create_default_https_context = ssl._create_unverified_context

username = "eapi"
password = "17mendel"
host = "184.105.247.75"

conn = Server("https://%s:%s@%s/command-api" %(username, password, host))

list_cmd = [ "enable", "configure", "show interfaces" ]

output = conn.runCmds(1, list_cmd, "text")

num_output = str(output[2]['output'])

#list_of_interfaces = re.findall('.* is .*[up|down], .*', num_output)

print num_output

