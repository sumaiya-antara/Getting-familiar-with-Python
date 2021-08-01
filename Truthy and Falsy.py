#Truthy and Falsy 
'''
is_old = bool('hello')
is_passed = bool(6)

print(bool(''))  #gives falsy value
print(bool(0))
'''

password = '1234'
username = 'jhonny'

if password and username:
  print('You are signed up for the portal!')
else:
  print('Please enter a username and password')