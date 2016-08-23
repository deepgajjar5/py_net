#!/usr/bin/env python

import snmp_helper
import pygal
import json
import os

ip_addr = "184.105.247.71"
username = "pysnmp"
auth_key = "galileo1"
encr_key = "galileo1"
snmp_port = 161

ip_tuple = (ip_addr, snmp_port)

user_tuple = (username, auth_key, encr_key)

def get_oid(ip_tuple, user_tuple, oid):
    snmp_data = snmp_helper.snmp_get_oid_v3(ip_tuple, user_tuple, oid)
    output = snmp_helper.snmp_extract(snmp_data)
    return output

def create_graph(lst1, lst2):
    line_chart = pygal.Line()
    line_chart.title = "Input/Output packets and bytes"
    line_chart.x_labels = [ str(i) for i in range(5, 65, 5) ] 
    line_chart.add('InBytes', lst1)
    line_chart.add('OutBytes', lst2)
    line_chart.render_to_file('output.svg')

def get_output(filename, in_octets_packets_total, out_octets_packets_total):
    filename = "/home/dgajjar/py_net/week3/" + filename
    lst1 = []
    dict1 = {}
    list_of_diff = []
    if filename.startswith("in"):
        octets_packets_total = in_octets_packets_total    
    else:
        octets_packets_total = out_octets_packets_total    

    with open(filename, "r") as f:   
        file_size = os.fstat(f.fileno()).st_size
        if file_size == 0:
            with open(filename, "w") as f:
                dict1[octets_packets_total] = 0
                lst1.append(dict1)
                json.dump(lst1, f)

            with open(filename, "r") as f:
                output = json.loads(f.read())
                        
        else: 
            with open(filename, "r") as f:
                lst1 = json.loads(f.read())
                if len(lst1) >= 12:
                    lst1 = lst1[-11:]
                    last_max_value = lst1[-1]
                    for k, v in last_max_value.items():
                        dict1[octets_packets_total] = int(octets_packets_total) - int(k)
                    lst1.append(dict1)

                else:
                    last_max_value = lst1[-1]
                    for k, v in last_max_value.items():
                        dict1[octets_packets_total] = int(octets_packets_total) - int(k)
                    lst1.append(dict1)

            with open(filename, "w") as f:
                json.dump(lst1, f)

            with open(filename, "r") as f:
                output = json.loads(f.read())

    for i in output:
        for k, v in i.items():
            list_of_diff.append(int(v))

    return list_of_diff

in_octets_packets_total = int(get_oid(ip_tuple, user_tuple, oid="1.3.6.1.2.1.2.2.1.10.5")) # of type string, convert to int
out_octets_packets_total = int(get_oid(ip_tuple, user_tuple, oid="1.3.6.1.2.1.2.2.1.16.5"))

filename1 = "in-octets-total.json"
filename2 = "out-octets-total.json"

in_octets_list = get_output(filename1, in_octets_packets_total, out_octets_packets_total)
out_octets_list = get_output(filename2, in_octets_packets_total, out_octets_packets_total)

create_graph(in_octets_list, out_octets_list)
