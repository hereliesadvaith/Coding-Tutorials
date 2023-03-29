friends = ["ross", "monica", "chandler", "joey", "rachel", "phoebe"]

# length of the list
print(len(friends))
# to add an item at index -1
friends.append("Advaith")
# to remove an item
friends.remove("Advaith")
# to add an item at specific index
friends.insert(1, "advaith")
# sort alphabetically or numerically
friends.sort()
# to select from index 2 to -1
print(friends[2:])
# to select from index 0 to 2
print(friends[0:3])

# Nested list
n_list = ["advaith", [0, 1, 2, 3]]
# to select specific item
print(n_list[0][1])

# add lists
print(n_list[1] + [9, 11, 20])  # type: ignore
# multiply items in list
print(["a"] * 3)

my_list = ["a", "d", "v", "a", "i", "t", "h"]

# to remove item
my_list[3:4] = []

# Enumerate : to get item and it's index from a list
for index, item in enumerate(my_list):
    print(index, item)
