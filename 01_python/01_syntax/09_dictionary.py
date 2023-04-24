marks: dict[str, int] = {"Maths": 22, "History": 32, "Science": 44}
print(f"Marks:{marks}")

for subject in marks.keys():
    print(subject)

for scores in marks.values():
    print(scores)

for x, y in marks.items():
    print(f"{x}: {y} / 50")

for x, y in marks.items():
    if y >= 25:
        print(f"{x}: Pass")
    else:
        print(f"{x}: Fail")

# to set value of "Maths" key
marks["Maths"] = 30
# to get the value of specific key
print(marks["Maths"])
print(marks.get("Science"))
print(marks.get("Java"))

# to delete a pair
del marks["Science"]

my_dict = {"apple": 5, "banana": 2, "orange": 7}

# using get() function to retrieve value of 'apple' key
apple_count = my_dict.get("apple")
print(apple_count)  # output: 5

# using get() function to retrieve value of 'grape' key (which doesn't exist)
grape_count = my_dict.get("grape")
print(grape_count)  # output: None

# using get() function to retrieve value of 'grape' key with default value of 0
grape_count = my_dict.get("grape", 0)
print(grape_count)  # output: 0
