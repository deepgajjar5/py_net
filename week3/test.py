import json
import os

dict1 = { "100100" : "110" }

lst1 = []
lst1.append(dict1)

with open("data.json", "w") as f:
    json.dump(lst1, f)

with open("data.json", "r") as f:
    output = json.loads(f.read())
    print type(output)


dict2 = { "110110" : "120" }

output.append(dict2)

with open("data.json", "w") as f:
    json.dump(output, f)

with open("data.json", "r") as f:
    output = json.loads(f.read())
    print output

for i in output:
    for k, v in i.items():
       print k, v 
