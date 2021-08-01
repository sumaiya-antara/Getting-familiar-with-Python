# '==' checks if the values are equal or not. 'is' checks if the location in memory where the values are stored,are same or not.
# Every time I create a list, it is stored in different location of the memory. Even if I create an another empty list, it will be stored in another location of the memory. So, if we print([] is []) ------it will give false output.
# Sets and dictionaries are also created in different locations of the memory each time we create.

print(bool(0))
print(True == True)
print(1 == 1)
print('' == '')

print([] is [])

print('5' is '5')
a = {
  'age' : 50,
  'name' : 'poki'
}

b = {
  'age' : 50,
  'name' : 'poki'
}

print(a is b)
print(a == b)

print(10 is 10.0)


