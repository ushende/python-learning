# - list basic 

# grocery_list = ['eggs', 'bread', 'butter'] # changing item from the list
# grocery_list[2] = 'ketchup'
# print(grocery_list)

# grocery_list = []  # adding item into list
# grocery_list.append('eggs')
# grocery_list.append('bread')
# grocery_list.append('butter')
# print(grocery_list)

# grocery_list = ['eggs', 'bread', 'butter'] # deleting item form the list
# print(grocery_list)
# del grocery_list[2]
# print(grocery_list)

# grocery_list = ['eggs', 'bread', 'butter'] # inserting item into list
# print(grocery_list)
# grocery_list.insert(3, 'ketchup') # (index-pos, 'item-name')
# print(grocery_list)

# grocery_list = ['eggs', 'bread', 'butter'] # popping/del item from the  list
# popped_item = grocery_list.pop(0) # store the pop item into variable 
# print("I don't like", popped_item) # use that pop item in sentence

# grocery_list = ['eggs', 'bread', 'butter'] # removing item by value from the list
# print(grocery_list)
# grocery_list.remove('eggs')
# print(grocery_list)


# - organizing a list

# grocery_list = ['eggs', 'bread', 'butter', 'ketchup'] # removing item by value from the list
# print("Here is original list.")
# print(grocery_list)

# grocery_list.sort() # organize the list in alphabetical order
# print("\nHere is sorted list.")
# print(grocery_list)

# grocery_list.reverse # organize the list in reverse order
# print("\nHere is reverse order list.")
# print(grocery_list)

# - length of list 

# print(len(grocery_list))
# item = len(grocery_list) # this will list number (int calculate item in list)
# print("There are " + str(item) + " items in the list.")


# - for loop basic

#This line tells Python to pull a name from the list grocery_list, and store it in the variable grocery.

# grocery_list = ['eggs', 'bread', 'butter', 'ketchup'] 
# for grocery in grocery_list: 
#     print(grocery)

# print("I'll use this items to make an ommelet.")

# - using range() function

# for value in range(1, 5):
#     print(value)

# numbers = list(range(1, 6))
# print(numbers)

# tables = list(range(2, 21, 2))
# print(tables)

# for tables in range(2, 21, 2):
#     print(tables)

# squares = []
# for value in range(1, 11):
#     square = value**2
#     squares.append(square)

# print(squares)

# squares = [value**2 for value in range(1, 11)] # list comprehension
# print(squares)

# simple statistics with the list numbers

# digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(min(digits))
# print(max(digits))
# print(sum(digits))

# for odd in range(1, 21, 2): # - start with (1) and you get odd number and start with 2 you get prime number
#     print(odd)

# -slicing list

# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# print(players[0:3]) # (start:stop:increament)
# print(players[1:4])
# print(players[2:3])
# print(players[:4])
# print(players[0:])
# print(players[-1:])
# print(players[-2:])
# print(players[-3:])

# print("Here are the first three players on my team:")
# for player in players[:3]:
#     print(player.title())


# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# player = players[:] # made a copy of list (players)

# print("Here is orginal list.")
# print(players) # orignal

# print("Here is copy list.")
# print(player) # copy
# player.append('manuel')
# print(player)


# tuple 

# dimension = (200, 50)
# print(dimension[0])
# print(dimension[1])

# dimension[0] = 100
# print(dimension[0]) # we cannot change tuple we have to redefine new tuple

# dimensions = (200, 50)
# for dimension in dimensions:
#     print(dimension)













































