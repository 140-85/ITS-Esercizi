# 4-15. Code Review: Choose three of the programs you’ve written in this chapter and modify each one to comply with PEP 8.

# 4-11
# Basic list
favorite_pizzas = [
    "Diavola",
    "Margherita",
    "Cacio & pepe",
    "4 Formaggi",
    "Broccoli & salsiccia",
]

# Copy of the list
friend_pizzas = favorite_pizzas[:]

# Added a new pizza to the basic list
favorite_pizzas.append("Mortadella & pistacchio")

# Added a new pizza to the friend's list
friend_pizzas.append("Marinara")

# Proof that they are separate lists
print("My favorite pizzas are:")
for pizza in favorite_pizzas:
    print(pizza)

print("\nMy friend’s favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)

# 4-1
# Pizzas list
favorite_pizzas = [
    "Diavola",
    "Margherita",
    "Cacio & pepe",
    "4 Formaggi",
    "Broccoli & salsiccia",
]

# For loop to print out the name of each pizza
for pizza in favorite_pizzas:
    print(f"I like {pizza}")

# Statement
print("I really love pizza!")

# 4-2
# Animals list
animals = [
    "Snake",
    "Mantis",
    "Ocelot",
    "Raven",
    "Wolf",
    "Octopus",
]

# For loop to print out the name of each animal
for animal in animals:
    print(f"A {animal} would make a great pet")

# Common characteristic
print("All of these animals are less dangerous than a cornered fox.")