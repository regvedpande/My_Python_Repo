# Question 1 :
# This program takes a message from the user and either encodes or decodes it based on the user's choice.
# The encoding process involves:
# - For words with 3 or more characters: moving the first character to the end and adding "dsf" at the beginning and "jsk" at the end.
# - For words with less than 3 characters: reversing the word.
# The decoding process involves:
# - For words with 3 or more characters: removing the first 3 characters and the last 3 characters, then moving the last character to the beginning.
# - For words with less than 3 characters: reversing the word.
st = input("Enter Message")
words = st.split(" ")
coding = input("1 for Coding or 0 for Decoding")
coding = True if (coding == "1") else False
if coding:
    nwords = []
    for word in words:
        if len(word) >= 3:
            r1 = "dsf"
            r2 = "jsk"
            stnew = r1 + word[1:] + word[0] + r2
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))
else:
    nwords = []
    for word in words:
        if len(word) >= 3:
            stnew = word[3:-3]
            stnew = stnew[:-1] + stnew[:-1]
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))
