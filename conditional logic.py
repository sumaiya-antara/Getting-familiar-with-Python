# When we use if, the interpreter will go inside the indentation only if the condition is fulfilled.
# The else block only runs if the if block of code evaluates to false.
# Programs may have a lots of elif (else if).

is_old =  True
is_licensed =  False

if is_old and is_licensed:
  print('You are old enough to drive and licensed')
elif is_old:
  print('You are old enough to drive but do not have license')
elif is_licensed:
  print('You are not old enough to drive')
else:
  print('Check again')

