# Drop your JSON file(s) into the current directory

import json

# Opens the JSON file as readable file and sets the variable 'f' to it
## Loads the contents of the json and sets it to 'data'

with open('test2.json', 'r') as f:
    data = json.load(f)

# Checks the JSON group
## Prints the selected subgroups

for users in data['users']:
    print(users['name'], users['email'])
        
