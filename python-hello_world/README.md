# Python Project

## Table of Contents

1. [Author's Disclaimer](#authors-disclaimer)
2. [Resources](#resources)
3. [Learning Objectives](#learning-objectives)
4. [Requirements](#requirements)
5. [Example Code](#example-code)
6. [More Info](#more-info)

---

## Author's Disclaimer

Welcome to the Python world!

In Python (and most high-level languages), there are often many ways to achieve the same result. Some tasks have a single implementation, while others offer multiple solutions. Python follows a style guide called **PEP8**, now also known as **Pycodestyle**. At Holberton, we won't enforce Pycodestyle initially as it is more strict than PEP8. If you see warnings when running PEP8, you can safely ignore them.

Enjoy!

---

## Resources

To help you get started, here are some resources to explore:

- **Learn to Program**
- **Whetting Your Appetite**
- **Using the Python Interpreter**
- **An Informal Introduction to Python** (up to section "3.1.2. Strings")
- **How To Use String Formatters in Python 3**
- **Pycodestyle – Style Guide for Python Code**

---

## Learning Objectives

By the end of this project, you should be able to explain the following concepts:

### General

- How to use the Python interpreter
- How to print text and variables using `print()`
- How to use strings in Python
- What indexing and slicing are in Python
- What the official Python coding style is and how to check your code with Pycodestyle

---

## Requirements

### Python Scripts

- **Allowed editors**: vi, vim, emacs
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3 (version 3.8.*)
- All your files should end with a new line.
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file must be present at the root of the repository, describing the project.
- Your code should conform to **pycodestyle** (version 2.7.*).
- All your files must be executable.
- The length of your files will be tested using `wc`.

---

## Example Code

Here is an example Python script that follows the PEP8 style guide:

```python
#!/usr/bin/python3

# This is an example of using print, strings, and indexing in Python

name = "Alice"
age = 30

# Print using f-string
print(f"Name: {name}, Age: {age}")

# Indexing to access the first letter of the name
print(f"First letter of name: {name[0]}")

# Slicing to get a substring of the name
print(f"First three letters 
