# Drop your JSON file(s) into the current directory (Use https://elmah.io/tools/json-formatter/ to validate your file)

import json

# Opens the JSON file as readable file and sets the variable 'f' to it
## Loads the contents of the json and sets it to 'data'

with open('INSERT .JSON FILE HERE', 'r') as f:
    data = json.load(f)

# Checks the JSON group
## Prints the selected subgroups

for users in data['INSERT MAIN GROUP NAME IN YOUR JSON FILE']:
    print(users['SUBGROUP 1'], users['SUBGROUP 2'])
    
# To insert into a .csv file use this...
import csv

with open('newContent.csv', 'w') as x:
    fieldName = data['ADD MAIN JSON GROUP'][0].keys()
    writer = csv.DictWriter(x,fieldnames=fieldName)
    writer.writeheader()
    for users in data['ADD MAIN JSON GROUP']:
        writer.writerow(users)
