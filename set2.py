'''
***Code 1***
-------  .difference() -------

my_set = {1,2,3,4}
your_set = {4,5,6,7,8}

print(my_set.difference(your_set))  # it shows the difference between my_set and your_set. Everything common between the two sets are wiped and the rest of the values of the my_set are shown in output.

'''

   

'''
***Code 2***
-------  .discard() ------- 

my_set = {1,2,3,4}
your_set = {4,5,6,7,8}

your_set.discard(7)   #It removes an element from a set if it is a member

print(your_set)

'''



'''
***Code 3***
-------  .difference_update() -------  
~~~~~~.difference() does not modify the set. .difference_update() modifies the set~~~~~~~

my_set = {1,2,3,4}
your_set = {4,5,6,7,8}

your_set.difference_update(my_set)  #it will remove all elements of my_set from your_set

print(your_set)

'''


'''
***Code 4***
-------  .intersection() ------- 

my_set = {1,2,3,4,5}
your_set = {4,5,6,7,8}

print(my_set.intersection(your_set))  #shows the common data between two sets by intersecting

      #or

print(my_set & your_set)

'''



'''
***Code 5***
-------  .isdisjoint() ------- 

my_set = {1,2,3,4,5}
your_set = {4,5,6,7,8}

print(my_set.isdisjoint(your_set))  #isdisjoint means the two sets have nothing in common. If the two sets have common items, the result will be False and if the two sets have nothing in common, the result will be True.

'''




'''
***Code 6***
-------  .union() ------- 

my_set = {1,2,3,4,5}
your_set = {4,5,6,7,8}

print(my_set.union(your_set))
     #or
print(my_set | your_set)

'''



'''
***Code 7***
-------  .issubset() ------- 

my_set = {4,5,6}
your_set = {4,5,6,7,8}

print(my_set.issubset(your_set))

'''



'''
***Code 8***
-------  .issuperset() ------- 
'''
my_set = {4,5,6}
your_set = {4,5,6,7,8}

print(my_set.issuperset(your_set))  #the answer will be false because for being superset, a set has to contain every items of other set.

print(your_set.issuperset(my_set))  #the answer will be true
