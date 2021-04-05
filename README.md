# LTU-Project S21
Team Members: Chayan Kochar, Tanishq Goel

## Topic: To find patterns in 500 sentences in English, Hindi, Telugu each.

---
### Data :

We have primarily used the data from the cfilt iitb website, the zip and folders of which are present in the repo named as "dev_test.tgz" and dev_test/
From the dev.en set we only got around 55 occurences of relative clause out of 500 sentences(put in "english_relcl.txt"). Hence we also ran on the test set which had roughly 2500 sentences - the sentences with rel clause is put "in english_relcl_testen" file.

Similarly for Hindi, from dev.hi, we got some 30 out of 500 dev set(put in "hindi_relcl.txt"). And on running the test.hi set(2.5k), we got 435 sentences with rel clause, and is put under "hindi_relcl_testhi.txt"

NOTE: 
- The running of the file over all the sentences very long time. Like for the 2.5k sentences, it almost took around 10 minutes or so even after running on colab!
- regarding telugu, we did not get any good sources for the data. Though once we get, i think we can simply apply the same code over it using stanza and shortlist the sentences and annotate it.

---

### Tasks for interim

- [X] Shortlist and annotate the sentences ( we did the shortlisting, and we did using certain dep features by stanza, so basically annotation is almost done, we just need to present it in a file)
- [x] Read through the literary section and other stuff(tbh, not totally done, but almost completed)
- [ ] Try to start code for finding patterns
