import stanza
import re


def get_dependencies(doc, n):
    """Get dependencies in the format of a list of
    (token, deprel, dependent_token) pairs-
    for all 'n' sentences in doc"""

    def getdeps(i):
        deps = []
        for head, rel, dep in doc.sentences[i].dependencies:
            deps.append((head.id, head.text, rel, dep.text, dep.id))
        return deps

    return [getdeps(i) for i in range(n)]


def get_pos_tags(doc, n):
    """Get POS-tagged tokens in the format of a list of
    (token, POStag) pairs for all sentences in doc.
    Returns upos (Universal part-of-speech) tag only, not
    xpos (treebank-specific part of speech)"""

    def getpos(i):
        tokens = []
        for token in doc.sentences[i].words:
            tokens.append((token.id, token.text, token.upos))
        return tokens

    return [getpos(i) for i in range(n)]


global relcl
relcl = []


def reltive_clause(deprel_list, pos_list, sent):
    for x in deprel_list:
        if (re.search(".*relcl.*", x[2])):
            relcl.append(sent)


# ==== MAIN: English ====
# This sets up a default neural pipeline in English
nlp_en = stanza.Pipeline('en')
nlp_hi = stanza.Pipeline('hi')
# english_data = ["The girl who is sitting there is my sister.",
#                 "The horse which Mary was riding is very friendly.",
#                 "We don’t know the person who donated this money.",
#                 "I like the shirt which is yellow in colour.",
#                 "If you know who did it, you should tell the teacher.",
#                 "Many Revenue department officials are continuously asking the Canadian Chartered Accountants to force foreigners to declare their income which they are earning in other countries, so that they can calculate the appropriate tax on the income they are earning in Canada."]

english_data = open("./dev.en", "r")
# hindi_data = open("./hindi_data.txt", "r")

for i in english_data:  # swap between english and hindi data accordingly
    # sentence = english_data.readline()
    doc = nlp_en(i)  # swap accordingly
    dep = (get_dependencies(doc, 1))
    # print(dep)
    pos = (get_pos_tags(doc, 1))
    # print(pos)
    # print("--------------")
    # for x in dep[0]:
    #     print(x)
    # print("dep done now pos------------")
    # for x in pos[0]:
    #     print(x)

    reltive_clause(dep[0], pos[0], i)

    
for z in relcl:
    f = open("./english_relcl.txt", "a")
    f.write(str(z) + "\n")
    f.close()



# ==== MAIN: Hindi ====

# this sets up a default neural pipeline for Hindi
# nlp_hi = stanza.Pipeline('hi')
# doc_hi = nlp_hi("नमस्ते तुम कैसे हो")

# # this accesses the list of Token objects in the sentence
# # for more on the data structures in a Document, see here:
# # https://stanfordnlp.github.io/stanza/data_objects.html
# #print(doc_hi.sentences[0].tokens)


# # this prints the dependency tree in a human-readable format
# #doc_hi.sentences[0].print_dependencies()

# # same set of functions as above- but for Hindi
# print(get_dependencies(doc_hi, 1))
# print(get_pos_tags(doc_hi, 1))
