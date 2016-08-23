import snmp_helper
import pickle
import json
import email_helper

ip_addr = "184.105.247.71"

snmp_port = 161

username = "pysnmp"

auth_key = "galileo1"

encrp_key = "galileo1"

sender = "deep@arista.com"
recipient = "deep.gajjar@colorado.edu"
subject = "Router Config changed"

ip_tuple = (ip_addr, snmp_port)

user_tuple = (username, auth_key, encrp_key)

snmp_data = snmp_helper.snmp_get_oid_v3(ip_tuple, user_tuple, oid="1.3.6.1.2.1.1.3.0")

sysuptime = snmp_helper.snmp_extract(snmp_data)

str_uptime = ""
str_uptime = str(sysuptime)

snmp_data = snmp_helper.snmp_get_oid_v3(ip_tuple, user_tuple, oid="1.3.6.1.4.1.9.9.43.1.1.1.0")

uptime_running_config_changed = snmp_helper.snmp_extract(snmp_data)

str_uptime_running_config = ""
str_uptime_running_config = str(uptime_running_config_changed)

with open("data-uptime.txt", "ab") as f1:
    f1.write(str_uptime + "\n")
    
with open("data-uptime-running.txt", "ab") as f2:
    f2.write(str_uptime_running_config + "\n")

uptime = []
uptime_running = []


with open("data-uptime.txt", "r") as f1:
    for line in f1:
        uptime.append(line)

with open("data-uptime-running.txt", "r") as f2:
    for line in f2:
        uptime_running.append(line)

new_uptime_running = []
new_uptime = []
if len(uptime_running) > 1:
    max_value_1 = max(uptime_running)
    new_uptime_running.append(max_value_1)
    uptime_running.remove(max_value_1)
    max_value_2 = max(uptime)
    new_uptime.append(max_value_2)
    uptime.remove(max_value_2)


    second_max_value_1 = max(uptime_running)
    new_uptime_running.append(second_max_value_1)
    uptime_running.remove(second_max_value_1)
    second_max_value_2 = max(uptime)
    new_uptime.append(second_max_value_2)
    uptime.remove(second_max_value_2)

    uptime = new_uptime
    
    uptime_running = new_uptime_running
    
    if uptime_running[0] != uptime_running[1]:
        print "Data has changed! Sending email"
        message = "Config change occured at " + (max(uptime))/100
        email_helper.send_mail(recipient, subject, message, sender)                  

    else:
        pass
    

else:
    pass



