# Python - More Data Structures: Set, Dictionary

## Project Overview

This project introduces key Python data structures: **Set** and **Dictionary**, and teaches their usage and differences. You'll also get familiar with important Python concepts like **lambda functions**, and built-in functions such as **map**, **reduce**, and **filter**.

By the end of this project, you'll have a solid understanding of when and how to use these data structures, and how they differ from other common data structures like **Lists**.

## Learning Objectives

At the end of this project, you are expected to be able to:

### General
- **Why Python programming is awesome**: Understand the advantages of using Python and why it's favored by many developers.
- **What are sets and how to use them**: Learn about sets, a powerful and efficient data structure for storing unique elements.
- **What are the most common methods of set and how to use them**: Explore methods like `.add()`, `.remove()`, `.union()`, etc.
- **When to use sets versus lists**: Understand the performance benefits of using sets for operations like membership testing and removing duplicates.
- **How to iterate into a set**: Learn how to loop through sets using loops and comprehensions.
- **What are dictionaries and how to use them**: Gain a solid understanding of Python dictionaries, a collection of key-value pairs.
- **When to use dictionaries versus lists or sets**: Discover when dictionaries are the best choice, especially when you need to associate keys with values.
- **What is a key in a dictionary**: Learn the concept of keys and values and how to access dictionary items using keys.
- **How to iterate over a dictionary**: Learn how to loop over dictionary items efficiently.
- **What is a lambda function**: Understand how to create and use lambda functions for concise one-liner functions.
- **What are the map, reduce and filter functions**: Learn how to use these functional programming tools to transform or filter data.

## Requirements

### General
- **Allowed editors**: `vi`, `vim`, `emacs`
- **Operating System**: All files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3.8.5.
- **File Requirements**:
  - All your files should end with a new line.
  - The first line of all your files should be exactly: `#!/usr/bin/python3`
  - A `README.md` file, located at the root of the project folder, is mandatory.
  - All your code should comply with the **pycodestyle** (version 2.7.*).
  - All your files must be executable.
  - The length of your files will be tested using `wc`.

## Resources

To help you succeed in this project, review the following resources:

1. [Data structures documentation](https://docs.python.org/3/tutorial/datastructures.html)
2. [Lambda, filter, reduce, and map](https://realpython.com/python-lambda/)
3. [Learn to Program 12: Lambda, Map, Filter, Reduce](https://www.youtube.com/watch?v=hYzwM0BdgYM)
4. Use the `man` or `help` commands in Python for more information:
   - `man python3`
   - `help()`

## Example

### Example 1: Working with Sets

A **set** is an unordered collection of unique elements. You can use it to eliminate duplicates from a list or to perform set operations.

```python
# Define a set
my_set = {1, 2, 3, 4, 5}

# Add an element to the set
my_set.add(6)

# Remove an element
my_set.remove(4)

# Union of two sets
another_set = {4, 5, 6, 7}
union_set = my_set.union(another_set)

# Print the results
print("Updated set:", my_set)      # {1, 2, 3, 5, 6}
print("Union of sets:", union_set)  # {1, 2, 3, 5, 6, 7}
