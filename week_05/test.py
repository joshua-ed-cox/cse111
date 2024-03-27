string1 = "anagram"
string2 = "naagram"

storted_string_1 = sorted(list(string1))
storted_string_2 = sorted(list(string2))

if storted_string_1 == storted_string_2:
    print("These are anagrams")
else:
    print("These are not anagrams")