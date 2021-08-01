# The function always has to return something.
# If we don't give 'return' in function, it will give None in output.
# A function either modifies soemthing in our program or returns something.
# As soon as we put return atthe function, it exists the function.

'''
def sum(num1, num2):
  return num1 + num2

total = sum(10,5)
print(sum(10, total))

'''
'''
def sum(num1, num2):
  return num1 + num2

print(sum(10,sum(10,5)))
'''

def sum(num1,num2):
  def another_func(n1,n2):
    return n1 + n2
  return another_func(num1, num2)

total = sum(10,20)
print(total)