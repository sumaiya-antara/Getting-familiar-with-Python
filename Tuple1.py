#Tuples
#Tuples are immutable. The values in tuple cannot be changed,sorted or reversed. We just can view it and look for it.
#Why should we use tuples instead of list?
#Answer: Tuples are safe. If I don't want others to change/modify my data, tuple is the best option to use. Tuples are also faster.

my_tuple = (1,2,3)
#my_tuple[1] = 'x'   #this will give an error
#print(my_tuple)
print(3 in my_tuple)  #We can do this operation

'''
user = {
  'basket': [3,4,5,6,7],
  'greet': 'hello',
  'year': 2021
}
'''

#print(user.items())  #This user.items() method returns the dictionary items in a tuple form.

user = {
  (2,4): [4,5,6,7,8], # As tuples are immutable, we can use tuples as a key in the dictionary like this.
  'name': 'Elina',
  'age': 22
}

print(user[(2,4)])     # We have to print like this in tuple key.
print(user[(2,4)][1])



