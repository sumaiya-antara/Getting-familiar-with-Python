# Enumerate prints the index number
# Enumerate is usefull as an index counter if we are looping an item.

'''
for i, char in enumerate([1,2,3,4]):
  print(i, char)

for i, char in enumerate("Hellooo"):
  print(i, char)
'''

for i, char in enumerate(list(range(100))):
  print(i, char)
  if char == 50:
    print(f'Index of 50 is: {i}')