from ciscoconfparse import CiscoConfParse

config = CiscoConfParse("cisco_ipsec.txt")

list1 = config.find_objects(r"^crypto map CRYPTO")

list2 = config.find_objects_w_child(parentspec=r"^crypto map CRYPTO", childspec=r"set pfs group2")

list3 = config.find_objects_wo_child(parentspec=r"^crypto map CRYPTO", childspec=r"set transform-set AES*")

for i in list1:
    for child in i.children:
        print child.text

for i in list2:
    for child in i.children:
        print child.text            

for i in list3:
    for child in i.children:
        print child.text
