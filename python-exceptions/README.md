# Python - Exceptions

![Project Badge](https://img.shields.io/badge/Project-Exceptions-Amateur)


---

## Description

This project focuses on understanding and working with **exceptions** in Python. You'll learn how to handle errors effectively, raise exceptions, and clean up after exceptions. This knowledge is essential for writing robust and error-free Python programs.

---

## Resources

Read or watch:

- [Errors and Exceptions](https://www.youtube.com/watch?v=NIWwJbo-9_8)
- [Learn to Program 11 Static & Exception Handling](https://www.youtube.com/watch?v=HHvIk9a9kmw) (starting at minute 7)

---

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General

- Why Python programming is awesome
- What’s the difference between errors and exceptions
- What are exceptions and how to use them
- When do we need to use exceptions
- How to correctly handle an exception
- What’s the purpose of catching exceptions
- How to raise a builtin exception
- When do we need to implement a clean-up action after an exception

---

## Requirements

### General

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the [pycodestyle](https://pypi.org/project/pycodestyle/) (version 2.7.*)
- All your files must be executable
- The length of your files will be tested using `wc`

---

## Example of Handling Exceptions in Python

Here is an example of how to handle an exception in Python:

```python
#!/usr/bin/python3

try:
    # Trying to divide by zero
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
finally:
    print("This will always be executed.")
