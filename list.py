#List

amazon_cart = [
 'notebook',
 'laptop', 
 'cable',
 'toys',
 'vase'
 ]

#print(amazon_cart[0:3])
#print(amazon_cart[2:5:2])
amazon_cart[0] = 'remote'
new_cart = amazon_cart[:]
new_cart[0] = 'pens'
print(new_cart)
print(amazon_cart)