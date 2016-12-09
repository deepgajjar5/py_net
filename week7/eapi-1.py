from jsonrpclib import Server
import sys
import ssl
import re
import csv
ssl._create_default_https_context = ssl._create_unverified_context

username = "eapi"
password = "17mendel"
host = "184.105.247.75"

conn = Server("https://%s:%s@%s/command-api" %(username, password, host))

list_cmd = [ "enable", "configure", "show interfaces" ]

output = conn.runCmds(1, list_cmd, "text")

num_output = str(output[2]['output'])

list_of_interfaces = re.findall('.* is .*[up|down], .*', num_output)

in_octets_list = re.findall('.* packets input, .* bytes', num_output)

out_octets_list = re.findall('.* packets output, .* bytes', num_output)

final_in_list = []
final_out_list = []
final_interface_list = []

for i in in_octets_list:
    final_in_list.append(i.split(',')[1])

for i in out_octets_list:
    final_out_list.append(i.split(',')[1])    

for i in list_of_interfaces:
    final_interface_list.append(i.split(" ")[0]) 

print final_in_list
print final_out_list
print final_interface_list


final_dict = {}
final_dict_list = []
final_dict_tuple = ();

for i in range(0, len(in_octets_list)):
    final_dict_list = [ final_in_list[i], final_out_list[i] ] 

    final_dict[final_interface_list[i]] = final_dict_list

    final_dict_list = [] 

print final_dict


