# 6-3. Glossary: A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.
# • Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store their meanings as values.
# • Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print the word on one line and then print its meaning indented on a second line. Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.

programming_terms = {
    'Variable': 'A storage location in programming that holds a value.',
    'Function': 'A block of code that performs a specific task when called.',
    'Loop': 'A programming structure that repeats a block of code as long as a condition is true.',
    'Array': 'A collection of elements identified by index or key.',
    'Class': 'A blueprint for creating objects in object-oriented programming.'
}

for word, meaning in programming_terms.items():
    print(f"{word}:\n  {meaning}\n")