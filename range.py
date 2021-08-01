# if the programmer does not need a variable in the for loop, just give an underscore(_) instead of the variable.
# Example: for _ in users:
'''
for _ in range(0, 10):
  print(_)
'''
'''
for _ in range(0, 10, 2):
  print(_)  #Here, 0 is the starting point of the loop, 10 denotes how many times the opeartion will be done and also the ending point is 10. 2 denotes the stepover.Default stepover is 1.
'''
for _ in range(10, 0, -1):
  print(_)  # for reversing, we have to give a negative stepover

for _ in range(3):
  print(list(range(12)))