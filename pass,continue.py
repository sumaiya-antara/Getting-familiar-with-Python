# Continue and Pass

#continue is useful for keeping the loop continued
# pass is used rarely. But it can be useful, if we want to keep  an loop opeartion on hold if we want to write it later.

'''
my_list = [1,2,3,4]

for item in my_list:
  continue
  print(item)   #the loop will keep going and nothing will be printed

i = 0
while i < len(my_list):
  continue
  i += 1
  print(my_list[i])  #the loop will keep going and nothing will be printed

  '''

my_list = [1,2,3,4]

for item in my_list:
  pass     #I am still thinking about it and will add it later

i = 0
while i < len(my_list):
  print(my_list[i])
  i += 1

