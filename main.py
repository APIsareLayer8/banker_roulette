import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")

# convert variable names_string into list called {names}
names = names_string.split(", ")

# get the length of the list and assign to new variable
num_in_list = len(names)

# generate a random number between 0 and the number of the last element in the list.
# Subtract one to account for index numbers. Example: A list with 5 elements has an index of 0 - 4.
random_name = random.randint(0, num_in_list - 1)

# attach the random generator to the list variable {names}
i_am_buying = names[random_name]

print(f'{i_am_buying} has to pay the bill!')
