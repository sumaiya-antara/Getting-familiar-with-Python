# Sets are unordered collections of unique objects
# Sets have values only, they don't have any key like dictionaries.
# In sets, there is no duplicate, everything/every value has to be unique.
# We can add data to set by .add() function
# Set objects do not support indexing, we cn look for/search set data by using 'in'

'''
***Code 1***

my_set = {1,2,3,4,5,6,4}
print(my_set) # This will only print {1,2,3,4,5,6} and will not print 4 twice.

'''



'''
***Code 2***

my_set = {1,2,3,4,5,6}
my_set.add(50)
my_set.add(99)
my_set.add(3) # 3 won't be added as it already exists

print(my_set)

'''




'''
***Code 3***
Forming a new set from a list, there will be no duplicate data:

my_list = [1,2,3,4,5,5]
print(set(my_list))

'''



'''
***Code 4***

my_set = {1,2,3,4,5,5}

#print(my_set[0])  #this will give error as set doesn't support indexing

print(2 in my_set)  # This will work

'''



'''
***Code 5***
We can print the length of a set.......

my_set = {1,2,3,4,5,5}
print(len(my_set))

'''


'''
***Code 6***
We can convert a set to a list also.......

my_set = {1,2,3,4,5,5}
print(list(my_set))

'''



'''
***Code 7***
We can copy a set by using .copy()..........
'''
my_set = {1,2,3,4,5,5}
new_set = my_set.copy()

print(new_set)
print(my_set)

my_set.clear()
print(my_set)  #this will return an empty set
