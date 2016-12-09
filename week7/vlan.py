import pyeapi
import ssl 
ssl._create_default_https_context = ssl._create_unverified_context
import argparse

conn = pyeapi.connect_to("pynet-sw4")

vlan_list = conn.enable("show vlan")

parser = argparse.ArgumentParser()

#args = parser.parse_args()

vlans = conn.api("vlans")

list_of_vlans = [] 

mydict = vlan_list[0]['result']['vlans']

for key in mydict:
    list_of_vlans.append(key)

parser.add_argument('--name', required=False, nargs = 2)

parser.add_argument('--remove', required=False, nargs = 1)

args = parser.parse_args()

if args.name != None:
    vlan_id = args.name[1]
    vlan_name = args.name[0]
    if vlan_id in list_of_vlans:
        print "Vlan is already present! Choose another vlan id"

    elif (int(vlan_id) < 100 or int(vlan_id) > 999):
        print "Vlan must lie between 100 and 999"

    else:
        print "Vlan %s will be added" %(vlan_id)
        vlans.create("%s" %(vlan_id))
        vlans.set_name("%s" (vlan_id), "%s" %(vlan_name))

else:
    remove_vlan_id = args.remove[0]
    if remove_vlan_id not in list_of_vlans:
        print "The vlan that you are trying to remove does not exist!"
    else:
        conn.config("no vlan %s" %(remove_vlan_id))

final_vlan_list = conn.enable("show vlan")
    
final_dict = final_vlan_list[0]['result']['vlans']

final_list_of_vlans = []

for key in final_dict:
    final_list_of_vlans.append(key)

print final_list_of_vlans

