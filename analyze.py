import json
f = open('annotated_english.json', 'r')
data = json.load(f)
relPronList = ["who", "whom", "which", "that",
               "those", "whose", "where", "when", "why", "what"]

# relPronList = ['जो', 'जोकि', 'जहाँ', 'जिधर', 'जितना', 'जितने', 'जैसा', 'जैसे', 'जिसको', 'जिसके',
#                'जिस', 'जिसे', 'जिससे', 'जिसकी', 'जिसका', 'जिसने', 'जिन्हें', 'जिन्होंने', 'जिसमें', 'जिनमें', 'जिनकी', 'जब']
nom_rel = 0
rel_nom = 0
red_rel = 0
f1 = open('outputs/english_nom_rel.txt', 'w')
f2 = open('outputs/english_rel_nom.txt', 'w')
f3 = open('outputs/english_red_rel.txt', 'w')
for j in data:
    for i in data[j]:
        if i == "sentence":
            continue
        if data[j][i]['deprel'] == 'acl:relcl':
            pronoun_present = False
            headID = data[j][i]['head']
            currentID = data[j][i]['id']
            for k in data[j]:
                if k == 'sentence':
                    continue
                if (data[j][k]['head'] == currentID):
                    if (data[j][k]['text'].lower() in relPronList):
                                    
                        if data[j][k]['id'] > headID:
                            nom_rel += 1
                            f1.write("Sentence "+str(j)+":")
                            f1.write(data[j]['sentence'])
                            f1.write("REL PRONOUN: \"" +
                                  data[j][k]['text']+"\" with ID: "+str(data[j][k]['id'])+"\n")

                            f1.write(
                                "REFERNT: \"" + data[j][str(data[j][i]['head'])]['text'] + "\" with ID :"+str(headID)+"\n\n")

                        else:
                            rel_nom += 1
                            f2.write("Sentence "+str(j)+":")
                            f2.write(data[j]['sentence'])
                            f2.write("REL PRONOUN: \"" +
                                     data[j][k]['text']+"\" with ID: "+str(data[j][k]['id'])+"\n")

                            f2.write(
                                "REFERNT: \"" + data[j][str(data[j][i]['head'])]['text'] + "\" with ID :"+str(headID)+"\n\n")

                        pronoun_present = True
            if pronoun_present == False:
                f3.write("Sentence "+str(j)+":")
                f3.write(data[j]['sentence'])
                f3.write("NO PRONOUN\n")
                f3.write(
                    "REFERNT: \"" + data[j][str(data[j][i]['head'])]['text'] + "\" with ID :"+str(headID)+"\n\n")
                red_rel += 1
f1.close()
f2.close()
f3.close()
print("==================================")
print("Nominal then relative pronoun: ", nom_rel)
print("Relative pronoun then nom: ", rel_nom)
print("instances of reduced relativization: ",red_rel)

