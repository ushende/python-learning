# --- first program 

# print("Hello world!")
# print("Hello, Python world!")
# print("Myself, Umesh Shende. I'm learning Python language.")


# --- variables - [variable hold value, which is related to that variable]

# age = 26  
# print(age)
# name = "Umesh Shende" 
# print(name)


# --- strings [string is simply a series of characters]

# print("This is a string.")   
# print("This is also a string.")

# changing cases in strings

# name = "umesh shende"
# print(name.title()) # title is method - each word begin with capital letter
# print(name.lower()) # with lower method each word convert into lowercase
# print(name.upper()) # with upper method each word convert into uppercase

# concatenating the strings

# first_name = "umesh"
# last_name = "shende"
# full_name = first_name + " " + last_name # concatenating the strings with (+)
# print("Hello, " + full_name.title() + "!")

# newline/tab

# print("\tPython") # \t - adds a tab to a text
# print("\nPython") # \n - adds a new line

# print("Grocert List:\n\tEggs\n\tBread\n\tKetchup\n\tButter") # first add newline then tab 


# --- intergers

# print(5 + 5) # addition
# print(5 - 5) # subtraction
# print(5 * 5) # multiply
# print(5 / 5) # division (this gives floating decimal value)

# print(5 // 5) # division (this give integer value)
# print(5 ** 5) # this mean 5 * 5 * 5 * 5 * 5

# print((2 + 3) * 4) # that paraentheses will give priority to that sum

# pi = 3.14
# message = "The value of pi is " + str(pi) # (we need to convert that interger into string with [str])
# print(message)


# --- this is how you write comment.


# --- list basic [change/append()/del/insert()/pop()/remove()]

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


# --- organizing a list (sorting/reverse)

# grocery_list = ['eggs', 'bread', 'butter', 'ketchup'] # removing item by value from the list
# print("Here is original list.")
# print(grocery_list)

# grocery_list.sort() #organize the list in alphabetical order
# print("\nHere is sorted list.")
# print(grocery_list)

# grocery_list.reverse #organize the list in reverse order
# print("\nHere is reverse order list.")
# print(grocery_list)


# --- length of list - len()

# print(len(grocery_list))
# item = len(grocery_list) # this will list number (int calculate item in list)
# print("There are " + str(item) + " items in the list.")


# --- for loop basic [for loop]

# grocery_list = ['eggs', 'bread', 'butter', 'ketchup'] 
# for grocery in grocery_list:  # for loop store grocery_list items in grocery with each loop
#     print(grocery) # then print each value 


# --- using range()

# tables = list(range(2, 21, 2)) # (start:stop:increament)
# print(tables)


# --- simple statistics with the list numbers [min/max/sum]

# digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(min(digits)) # min give minimum number form the list
# print(max(digits)) # max give maximum number form the list
# print(sum(digits)) # sum give sum of all the number from the list


# --- slicing list - [start:stop:increament]

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


# m--- create a copy of list [:]

# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# player = players[:] # made a copy of list (players)

# print("Here is orginal list.")
# print(players) # orignal

# print("Here is copy list.")
# print(player) # copy
# player.append('manuel')
# print(player)


#--- tuple [tuple can't be changed]

# dimension = (200, 50)
# print(dimension[0])
# print(dimension[1])

# dimensions = (200, 50)
# for dimension in dimensions: # looping in tuple
#     print(dimension)


