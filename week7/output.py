from jsonrpclib import Server
import sys
import ssl
import re
import pyeapi
ssl._create_default_https_context = ssl._create_unverified_context

username = "eapi"
password = "17mendel"
host = "184.105.247.75"

list_of_vlans = []

#conn = pyeapi.connect_to("pynet-sw4")

#vlans = conn.api("vlans")

#all_vlans = vlans.getall()

#for key, value in all_vlans.iteritems():
    #print key

conn = Server("https://%s:%s@%s/command-api" %(username, password, host))

list_cmd = [ "enable", "configure", "show vlan" ]

output = conn.runCmds(1, list_cmd, "text")

print output[2]['output'].split('\n')[2:]
