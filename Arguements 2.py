# These are positional Arguements.
'''
def say_hello(name, emoji):
  print(f'Hello {name}{emoji}')

#Arguements
say_hello('Antara', '^_^')
'''

#Default Parameters:
#Default parameters will provide the default values even if any arguements are not passed while calling the function. 

'''
def say_hello(name='Darth Vader', emoji='>_<'):
  print(f'Hello {name}{emoji}')

#Arguements
say_hello()
'''

#Keyword Arguements
#Keyword Arguements are arguments that can be called by their name. The position of the each arguements do not matter and the values are printed just like the way they are declared in the parameters. 

def say_hello(name, emoji):
  print(f'Hello {name}{emoji}')

#Arguements
say_hello(emoji = '^_^', name = 'Ryan')



