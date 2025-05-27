""" 5-2. More Conditional Tests: You don’t have to limit the number of tests you cre-
ate to 10. If you want to try more comparisons, write more tests and add them
to conditional_tests.py. Have at least one True and one False result for each of
the following:
• Tests for equality and inequality with strings
• Tests using the lower() method
• Numerical tests involving equality and inequality, greater than and less
than, greater than or equal to, and less than or equal to
• Tests using the and keyword and the or keyword
• Test whether an item is in a list
• Test whether an item is not in a list """

fruit = "banana"

print("Is fruit == 'banana'? I predict True.")
print(fruit == "banana")

print("\nIs fruit != 'apple'? I predict True.")
print(fruit != "apple")

print("\nIs fruit == 'Banana'? I predict False.")
print(fruit == "Banana")

print("\nIs fruit.lower() == 'banana'? I predict True.")
print(fruit.lower() == "banana")

print("\nIs fruit.lower() == 'BANANA'? I predict False.")
print(fruit.lower() == "BANANA")

number = 42

print("\nIs number == 42? I predict True.")
print(number == 42)

print("\nIs number != 100? I predict True.")
print(number != 100)

print("\nIs number > 30? I predict True.")
print(number > 30)

print("\nIs number < 10? I predict False.")
print(number < 10)

print("\nIs number >= 42? I predict True.")
print(number >= 42)

print("\nIs number <= 41? I predict False.")
print(number <= 41)

age = 25

print("\nIs age > 18 and age < 30? I predict True.")
print(age > 18 and age < 30)

print("\nIs age < 20 or age > 30? I predict False.")
print(age < 20 or age > 30)

colors = ["red", "blue", "green", "yellow"]

print("\nIs 'blue' in colors? I predict True.")
print("blue" in colors)

print("\nIs 'purple' in colors? I predict False.")
print("purple" in colors)

print("\nIs 'black' not in colors? I predict True.")
print("black" not in colors)

print("\nIs 'green' not in colors? I predict False.")
print("green" not in colors)