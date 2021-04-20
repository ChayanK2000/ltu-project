import json
f = open('annotated.json', 'r')
data = json.load(f)

for j in data:

    for i in data[j]:
        if data[j][i]['deprel'] == 'acl:relcl':
            print(data['1'][i])