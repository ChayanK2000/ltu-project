# LTU-Project S21
Team Members: Chayan Kochar, Tanishq Goel

## Topic: To find patterns and learn more about relative clause construction in 500 sentences in English, Hindi, Telugu each.

---
### Data :

We have primarily used the en-hi parallel data from the cflit iitb website, the zip and folders of which are present in the repo named as "dev_test.tgz" and dev_test/
From the dev.en set we only got around 55 occurences of relative clause out of 500 sentences(put in "english_relcl.txt"). Hence we also ran on the test set which had roughly 2500 sentences - the sentences with rel clause is put "in english_relcl_testen" file.

Similarly for Hindi, from dev.hi, we got some 30 out of 500 dev set(put in "hindi_relcl.txt"). And on running the test.hi set(2.5k), we got 435 sentences with rel clause, and is put under "hindi_relcl_testhi.txt"


Directory structure:
.
-> Data/
    -> english*.txt
    -> hindi*.txt
-> final_annotated_data/
    -> english_annotated.txt
    -> hindi_annotated.txt
-> main.py(for converting the annoattions to json)
-> annotate.py(for annotating and storing it in .txt files)
-> try.py(for analysing using json)
-> concatenate.py(random file for preprocessing)
-> annotated_english.json
-> annotated_hindi.json
-> outputs/
    -> english*.txt
    -> hindi*.txt
-> LTU_ProjectReport.pdf
....other not so relevant files


