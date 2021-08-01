#If a key does not exist in the dictionary, if we try to print the key---it will provide an error.
# To avoid the error, we use .get method in the print function with or without a default value. 

user = {
  'basket': [3,4,5],
  'message': 'Hello, there',
  'age': 25   #if we add the 'age' key in dictionary, the dictionary value will be shown in the output when we print
}

#print(user['age'])  #this line will give an key error

#print(user.get('age'))  #it will show None in output

print(user.get('age', 50))  #it will set and show  the default value of age if it doesn't exist in teh dictionary
