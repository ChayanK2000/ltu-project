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


global sov
global svo
global vos
global vso
global osv
global ovs
sov = []
svo = []
ovs = []
osv = []
vso = []
vos = []


def subobverb_order(deprel_list, pos_list, sent):

    for x in pos_list:
        if (re.search(".*VERB.*", x[2])):
            check_subj = 0
            check_obj = 0
            for y in deprel_list:
                ind_v = y[0]
                word_v = y[1]
                if(ind_v == x[0]):
                    # regex to handle different types of nsubj/csubj
                    if ((re.search(".*nsubj.*", y[2])) or (re.search(".*csubj.*", y[2]))):
                        check_subj = 1
                        ind_s = y[4]
                        word_s = y[3]

                    # thought to include obl as well but was not sure
                    if (('obj' in y[2]) or ('iobj' in y[2]) or ('ccomp' in y[2]) or ('xcomp' in y[2])):
                        check_obj = 1
                        ind_o = y[4]
                        word_o = y[3]

                    if (check_obj == 1 and check_subj == 1):
                        check_obj = 0
                        check_subj = 0
                        if(ind_s < ind_o):
                            if (ind_v < ind_s):
                                vso.append(
                                    (sent, (ind_v, word_v, ind_s, word_s, ind_o, word_o)))
                            elif (ind_v > ind_o):
                                sov.append(
                                    (sent, (ind_v, word_v, ind_s, word_s, ind_o, word_o)))
                            else:
                                svo.append(
                                    (sent, (ind_v, word_v, ind_s, word_s, ind_o, word_o)))
                        else:
                            if (ind_v < ind_s):
                                vos.append(
                                    (sent, (ind_v, word_v, ind_s, word_s, ind_o, word_o)))
                            elif (ind_v > ind_o):
                                osv.append(
                                    (sent, (ind_v, word_v, ind_s, word_s, ind_o, word_o)))
                            else:
                                ovs.append(
                                    (sent, (ind_v, word_v, ind_s, word_s, ind_o, word_o)))


global an
global na
an = []
na = []


def NA_order(deprel_list, pos_list, sent):
    for x in pos_list:
        if (re.search(".*ADJ.*", x[2])):
            check_n = 0
            for y in deprel_list:
                ind_a = y[4]
                word_a = y[3]
                if (ind_a == x[0]):
                    if ('amod' in y[2]):
                        check_n = 1
                        ind_n = y[0]
                        word_n = y[1]
                    if (check_n == 1):
                        check_n = 0
                        if (ind_a < ind_n):
                            an.append((sent, (ind_a, word_a, ind_n, word_n)))
                        else:
                            na.append((sent, (ind_a, word_a, ind_n, word_n)))


global ng
global gn
ng = []
gn = []


def GN_order(deprel_list, pos_list, sent):
    for x in deprel_list:
        if (re.search(".*nmod.*", x[2])) and (pos_list[x[0]-1][2] == 'NOUN' or pos_list[x[0]-1][2] == 'PRON' or pos_list[x[0]-1][2] == 'PROPN'):
            if x[0] < x[4]:
                ng.append((sent, (x[0], x[1], x[3], x[4])))
            else:
                gn.append((sent, (x[0], x[1], x[3], x[4])))


global adv_v
global v_adv
adv_v = []
v_adv = []


def ADV_order(deprel_list, pos_list, sent):
    for x in deprel_list:
        if (re.search(".*adv.*", x[2])) and (pos_list[x[0]-1][2] == 'VERB' or pos_list[x[0]-1][2] == 'AUX'):
            if x[0] < x[4]:
                v_adv.append((sent, (x[0], x[1], x[3], x[4])))
            else:
                adv_v.append((sent, (x[0], x[1], x[3], x[4])))


global aux_v
global v_aux
aux_v = []
v_aux = []


def AUX_order(deprel_list, pos_list, sent):
    for x in pos_list:
        if (re.search(".*VERB.*", x[2])):
            check_aux = 0
            for y in deprel_list:
                ind_v = y[0]
                word_v = y[1]
                if (ind_v == x[0]):
                    if ('aux' in y[2]):
                        check_aux = 1
                        ind_aux = y[4]
                        word_aux = y[3]
                    if (check_aux == 1):
                        check_aux = 0
                        if (ind_aux < ind_v):
                            aux_v.append(
                                (sent, (ind_aux, word_aux, ind_v, word_v)))
                        else:
                            v_aux.append(
                                (sent, (ind_aux, word_aux, ind_v, word_v)))


global relcl
relcl = []


def reltive_clause(deprel_list, pos_list, sent):
    for x in deprel_list:
        if (re.search(".*relcl.*", x[2])):
            relcl.apend(sent)


# ==== MAIN: English ====
# This sets up a default neural pipeline in English
nlp_en = stanza.Pipeline('en')
nlp_hi = stanza.Pipeline('hi')
# english_data = ["The girl who is sitting there is my sister.",
#                 "The horse which Mary was riding is very friendly.",
#                 "We don’t know the person who donated this money.",
#                 "I like the shirt which is yellow in colour.",
#                 "If you know who did it, you should tell the teacher."]

english_data = open("./english_data.txt", "r")
# hindi_data = open("./hindi_data.txt", "r")

for i in english_data:  # swap between english and hindi data accordingly
    # sentence = english_data.readline()
    doc = nlp_en(i)  # swap accordingly
    dep = (get_dependencies(doc, 1))
    print(dep)
    pos = (get_pos_tags(doc, 1))
    print(pos)
    print("--------------")
    for x in dep[0]:
        print(x)
    print("dep done now pos------------")
    for x in pos[0]:
        print(x)
    
    reltive_clause(dep[0], pos[0], i)

    # subobverb_order(dep[0], pos[0], i)
    # NA_order(dep[0], pos[0], i)
    # GN_order(dep[0], pos[0], i)
    # ADV_order(dep[0], pos[0], i)
    # AUX_order(dep[0], pos[0], i)
for z in relcl:
    f = open("./english_relcl.txt", "a")
    f.write(str(z) + "\n")
    f.close()

# for z in sov:
#     # swap between english_*.txt to hindi_*.txt
#     f = open("./english_result/english_sov.txt", "a")
#     f.write(str(z) + "\n")
#     f.close()
# for z in svo:
#     # swap between english_*.txt to hindi_*.txt
#     f = open("./english_result/english_svo.txt", "a")
#     f.write(str(z) + "\n")
#     f.close()
# for z in vso:
#     # swap between english_*.txt to hindi_*.txt
#     f = open("./english_result/english_vso.txt", "a")
#     f.write(str(z) + "\n")
#     f.close()

# for z in ovs:
#     # swap between english_*.txt to hindi_*.txt
#     f = open("./english_result/english_ovs.txt", "a")
#     f.write(str(z) + "\n")
#     f.close()
# for z in vos:
#     # swap between english_*.txt to hindi_*.txt
#     f = open("./english_result/english_vos.txt", "a")
#     f.write(str(z) + "\n")
#     f.close()
# for z in osv:
#     # swap between english_*.txt to hindi_*.txt
#     f = open("./english_result/english_osv.txt", "a")
#     f.write(str(z) + "\n")
#     f.close()

# for z in ng:
#     # swap between english_*.txt to hindi_*.txt
#     f = open("./english_result/english_ng.txt", "a")
#     f.write(str(z) + "\n")
#     f.close()
# for z in gn:
#     # swap between english_*.txt to hindi_*.txt
#     f = open("./english_result/english_gn.txt", "a")
#     f.write(str(z) + "\n")
#     f.close()

# for z in an:
#     # swap between english_*.txt to hindi_*.txt
#     f = open("./english_result/english_an.txt", "a")
#     f.write(str(z) + "\n")
#     f.close()
# for z in na:
#     # swap between english_*.txt to hindi_*.txt
#     f = open("./english_result/english_na.txt", "a")
#     f.write(str(z) + "\n")
#     f.close()

# for z in adv_v:
#     # swap between english_*.txt to hindi_*.txt
#     f = open("./english_result/english_adv_v.txt", "a")
#     f.write(str(z) + "\n")
#     f.close()
# for z in v_adv:
#     # swap between english_*.txt to hindi_*.txt
#     f = open("./english_result/english_v_adv.txt", "a")
#     f.write(str(z) + "\n")
#     f.close()

# for z in aux_v:
#     # swap between english_*.txt to hindi_*.txt
#     f = open("./english_result/english_aux_v.txt", "a")
#     f.write(str(z) + "\n")
#     f.close()
# for z in v_aux:
#     # swap between english_*.txt to hindi_*.txt
#     f = open("./english_result/english_v_aux", "a")
#     f.write(str(z) + "\n")
#     f.close()

# print("NO OF INSTANCES OF THE PATTERNS:")
# print("SOV", len(sov))
# print("SVO", len(svo))
# print("OSV", len(osv))
# print("OVS", len(ovs))
# print("VOS", len(vos))
# print("VSO", len(vso))
# print("SUBJECT OBJECT", len(svo) + len(sov) + len(vso))
# print("OBJECT SUBJECT", len(vos) + len(ovs) + len(osv))
# print("-----------")
# print("NOUN GENITIVE", len(ng))
# print("GENITIVE NOUN", len(gn))
# print("-----------")
# print("ADJ NOUN", len(an))
# print("NOUN ADJ", len(na))
# print("-----------")
# print("VERB ADVERB", len(v_adv))
# print("ADVERB VERB", len(adv_v))
# print("-----------")
# print("AUX VERB", len(aux_v))
# print("VERB AUX", len(v_aux))

# print(sov)
# print(svo)
# print(osv)
# print(ovs)
# print(vso)
# print(vos)
# print("------------")
# print(an)
# print(na)
# print("--------------")
# print(ng)
# print(gn)
# print("---------")
# print(v_adv)
# print(adv_v)
# print("---------")
# print(v_aux)
# print(aux_v)


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
