import json
f = open('annotated_hindi.json', 'r')
data = json.load(f)
# relPronList = ["who", "whom", "which", "that",
#                "those", "whose", "where", "when", "why", "what"]

relPronList = ['जो', 'जोकि', 'जहाँ', 'जिधर', 'जितना', 'जितने', 'जैसा', 'जैसे', 'जिसको', 'जिसके',
               'जिस', 'जिसे', 'जिससे', 'जिसकी', 'जिसका', 'जिसने', 'जिन्हें', 'जिन्होंने', 'जिसमें', 'जिनमें', 'जिनकी', 'जब']
for j in data:
#for every sentence in data
    print("\nSentence ", j, ":")
    print(data[j]['sentence'])
    for i in data[j]:
        #for every word(by index starting from 1) in sentence. it also has the key "sentence"
        if i == "sentence":
            continue
        if data[j][i]['deprel'] == 'acl:relcl':
            pronoun_present = False
            # print(data[j][i]['id'], data[j][i]['text'], data[j][i]['head'], data[j][str(data[j][i]['head'])]['text'])
            headID = data[j][i]['head']
            currentID = data[j][i]['id']
            for k in data[j]:
                if k == 'sentence':
                    continue
                if (data[j][k]['head'] == currentID):
                    if (data[j][k]['text'].lower() in relPronList):
                        print("REL PRONOUN: \"" +
                              data[j][k]['text']+"\" with ID: ", data[j][k]['id'])
                        print(
                            "REFERNT: \"" + data[j][str(data[j][i]['head'])]['text'] + "\" with ID :", headID)
                        pronoun_present = True
            if pronoun_present == False:
                print("no pronoun")
                print(
                    "REFERNT: \"" + data[j][str(data[j][i]['head'])]['text'] + "\" with ID :", headID)
