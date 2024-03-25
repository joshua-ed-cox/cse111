string = list("rat")
string2 = list("car")

string.sort()
string2.sort()

if string != string2:
    print("This is not an anagram")
else:
    print("This is an anagram")