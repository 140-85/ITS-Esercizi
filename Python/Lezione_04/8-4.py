# 8-4. Large Shirts: Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.

def make_shirt(size = "Large", message = "I love Python"):
    print(f"The shirt size is {size} and the message on it is: '{message}'")

make_shirt()

make_shirt("Medium")

make_shirt("Small", "FREE LUIGI MANGIONE")