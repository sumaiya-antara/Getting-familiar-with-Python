# using this list, 
basket = ["Banana", "Apples", "Oranges", "Blueberries"];

# 1. Remove the Banana from the list

# 2. Remove "Blueberries" from the list.

# 3. Put "Kiwi" at the end of the list.

# 4. Add "Apples" at the beginning of the list

# 5. Count how many apples in the basket

# 6. empty the basket

#print(basket)

#basket.pop(0)
print(basket)
basket.pop(3)
print(basket)
basket.append('Kiwi')
print(basket)
basket.insert(0, 'Apples')
print(basket)

apples = basket.count('Apples')

print(apples)
basket.clear()
print(basket)