# code to remove all duplicates and concatenating the two files
f1 = open('hindi_relcl_dev.txt', 'r')
f2 = open('hindi_relcl_test.txt', 'r')
f3 = open('hindi_final.txt','w')
raw1 = f1.read()
raw1 = raw1.rstrip("\n")
raw1 = raw1.splitlines()
f1.close()
raw2 = f2.read()
raw2 = raw2.rstrip("\n")
raw2 = raw2.splitlines()
f2.close()
raw1 = list(set(raw1))
raw2 = list(set(raw2))
raw = raw1 + raw2
for i in raw:
    f3.write(i + "\n")
f3.close()

