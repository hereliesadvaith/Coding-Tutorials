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

# to del a pair
del marks["Science"]
