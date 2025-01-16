# Python - if/else, loops, functions

This project will help you learn and practice basic Python control flow concepts, such as `if` statements, loops, functions, and more. By the end of this project, you should be comfortable using these tools to write Python code that solves problems with proper structure and logic.

## Learning Objectives

By the end of this project, you will be able to:

- Understand the importance of indentation in Python.
- Use `if`, `if...else` statements for conditional logic.
- Add comments to explain your code.
- Assign values to variables.
- Use `while` and `for` loops to iterate over data.
- Implement `break`, `continue`, and `else` in loops.
- Understand and use the `pass` statement.
- Use the `range()` function in loops.
- Define and call functions, including understanding the return value.
- Understand variable scope in Python.
- Recognize and handle tracebacks.
- Use basic arithmetic operators.

## Resources

### Read or Watch:
- [More Control Flow Tools (until "4.6. Defining Functions")](https://docs.python.org/3/tutorial/controlflow.html)
- [IndentationError](https://realpython.com/python-indentation-errors/)
- [How to Use String Formatters in Python 3](https://realpython.com/python-f-strings/)
- [Learn to Program 2 : Looping](https://www.learnpython.org/)
- [Pycodestyle – Style Guide for Python Code](https://pep8.org/)

### Command-Line Resources:
- `python3` command for running Python scripts.
- `man` or `help` command for Python documentation.

## Requirements

- **Python Version**: 3.8.* (Ubuntu 20.04 LTS).
- **Editors**: vi, vim, emacs.
- **File Requirements**:
  - Files should end with a new line.
  - First line should be exactly `#!/usr/bin/python3`.
  - All files must be executable.
  - Code should comply with `pycodestyle` (version 2.7.*).

## Example Code

Here’s a simple example demonstrating control flow with `if`, `else`, loops, and functions.

```python
#!/usr/bin/python3

# Example function using if/else and loops
def check_numbers(limit):
    for i in range(limit):
        if i % 2 == 0:
            print(f"{i} is even")
        else:
            print(f"{i} is odd")
    
    # Use break and continue
    for i in range(5):
        if i == 3:
            continue  # Skip 3
        elif i == 4:
            break  # Exit loop
        print(i)

# Calling the function
check_numbers(10)
