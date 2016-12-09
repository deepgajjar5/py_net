from jsonrpclib import Server
import sys
import ssl
import re

with open("file1.txt", "r+") as f:
    output = f.read()

print re.findall('.* is up.*', output)
