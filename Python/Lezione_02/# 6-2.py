# 6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers. Think of five names, and use them as keys in your dictionary. Think of a favorite number for each person, and store each as a value in your dictionary. Print each person’s name and their favorite number. For even more fun, poll a few friends and get some actual data for your program.

favorite_numbers = {
    'Alice': 7,
    'Bob': 14,
    'Charlie': 21,
    'Diana': 3,
    'Eve': 9
}

for name, number in favorite_numbers.items():
    print(f"{name}'s favorite number is {number}.")