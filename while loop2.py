# While loop is very useful for cases where looping is needed for a long time.
# For loop is easier/simpler
# While loops are powerful

'''
my_list = [1,2,3,4]

for item in my_list:
  print(item)

i = 0
while i < len(my_list):
  print(my_list[i])
  i += 1
'''

while True:
  response = input("Say something: ")
  if(response == 'bye'):
    break
