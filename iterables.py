#Iterables
#Iterable is an object or a collection that can be iterated over. 

# sets, lists, tuples, dictionary, string are iterables. These are iterable because they can be iterated.Iterated means we can go one by one to check the collection.

#Iterable is the object or item, iterate is the action over iterable.

#We can print the keys and values together in different variables in the same loop

# int values are not iterable. Becaue they are not collections. For being iterable, it must be a collection of objects.

user = {
  'name': 'antara',
  'age': 24,
  'can_swim': False
}

for item in user:
  print(item)  #this will only print the keys

for item in user.items():
  print(item)  #this will print the whole dictionary

for item in user.values():
  print(item)  #this will print the values

for item in user.keys():
  print(item)

for key, value in user.items():
  print(key, value)

#We can also write like this

for k, v in user.items():
  print(k, v)

for item in 50:
  print(item)  #this will give an error as int values are not iterable.
