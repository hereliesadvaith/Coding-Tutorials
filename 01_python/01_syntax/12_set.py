magic_word = "avrakadavra"
unique_alphabets: set[str] = set(magic_word)
print(unique_alphabets)

sentence = "Iam gonna be a millionaire"
word_list = sentence.split()
print(word_list)
x: set[str] = set(word_list)
print(x)
x.update(["big", "can", "surely"])
print(x)
x.remove("big")
print(x)
