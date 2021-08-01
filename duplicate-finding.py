# Finding the duplicate items in a list
# count allows us to count how many times an item in a list exists.

some_list = ['a','b','c','b','d','e','f','e']

duplicates = []

for value in some_list:
  if some_list.count(value) > 1:
    if value not in duplicates:
      duplicates.append(value)

print(duplicates)