from pprint import pprint 
import json
import yaml

list1 = [ { 'deep' : 'gajjar', 'priti' : 'gajjar', 'sharvil' : 'gajjar', '12345' : 'digits' }, 1, 2, "xyz" ]

list2 = []

list3 = []

with open("json-str.txt", "w+") as f:
    json.dump(list1, f)

with open("yaml-str.txt", "w+") as f:
    yaml.dump(list1, f, default_flow_style=False)

with open("json-str.txt", "r") as f:
    list2 = json.load(f)

print pprint(list2)

with open("yaml-str.txt", "r") as f:
    list3 = yaml.load(f)

print pprint(list3)
