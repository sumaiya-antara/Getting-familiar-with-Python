#Searching/looking for an item in dictionary by using keyword 'in'

user = {
  'basket': [3,4,5],
  'message': 'Hello, there',
  'age': 25  
}
'''
print('age' in user)
print('size' in user)
print('size' in user.keys()) # looks for the keys
print(25 in user.values()) #looks for values
print(user.items())  # looks for the whole item in the dictionary
'''

#user.clear()  # Note: clears the items in dictionary and creates an empty dictionary
#print(user)

#user2 = user.copy()  # Note: it copies the whole dictionary
#print(user)
#print(user2)

#print(user.pop('age'))  # Note: user.pop() returns the value it removed

#print(user)  # age does not exist anymore

#print(user.popitem())  # Note: popitem will randomly remove some items fro the dictionary. We must be careful while using this method

print(user)

print(user.update({'age': 55})) # it will update the value in dictionary, update method can take at most 1 key-value pair at a time.
print(user)

print(user.update({'location': 'Mirpur'}))
print(user)



