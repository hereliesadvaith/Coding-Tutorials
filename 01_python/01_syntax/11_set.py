magic_word = "avrakadavra"
# to get unique alphabets in the string -- set of string
unique_alphabets: set[str] = set(magic_word)
print(unique_alphabets)

sentence = "Iam gonna be a millionaire before 24"
# to split the sentence into list of words
word_list = sentence.split()
print(word_list)
# to get unique items in the list -- set of list
x: set[str] = set(word_list)
print(x)
# to add items in the set
x.update(["big", "can", "surely"])
# to remove item from the set
x.remove("big")
