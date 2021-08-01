#Tuples can be sliced
# Tuples have two methods only: count(), index()

'''
***Code 1***
my_tuple = (1,2,3,4,5,6)
new_tuple = my_tuple[2:3]
print(new_tuple) 

'''
# The output would be ---(3,) because while printing single value, a comma is given after the value. 
'''
***Code 2***
my_tuple = (1,2,3,4,5,6)
new_tuple = my_tuple[2:5]
print(new_tuple) 
'''
# Here, the output would be as usual

'''
***Code 3***
x,y,z, *other = (1,2,3,4,5)
print(x)
print(y)
print(z)
print(*other)
'''


#***Code 4***

my_tuple = (1,2,6,3,2,4,5,6,1,4,5,6,2,3,5)
print(my_tuple.count(4))
print(my_tuple.count(5))
print(my_tuple.index(5)) #this will print the 1st index of that specific value
print(len(my_tuple))
