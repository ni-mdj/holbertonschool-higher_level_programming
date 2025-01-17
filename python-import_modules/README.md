# Python - Modules and Command Line Arguments

## Description

This project focuses on enhancing the understanding of using Python modules, importing functions, handling command-line arguments, and structuring Python programs. By the end of this project, you will be able to explain how to import and use modules in your Python programs, create modules, and understand how command-line arguments work.

### Learning Objectives

By the end of this project, you should be able to:
- Understand why Python programming is awesome.
- Import functions from another file.
- Use imported functions in your code.
- Create a Python module.
- Use the built-in `dir()` function.
- Prevent code in your script from executing when imported as a module.
- Use command-line arguments in your Python programs.

## Resources

- [Python Modules](https://docs.python.org/3/tutorial/modules.html)
- [Command-line Arguments](https://docs.python.org/3/library/sys.html#sys.argv)
- [Pycodestyle – Python Code Style Guide](https://www.python.org/dev/peps/pep-0008/)
- [man python3](https://man7.org/linux/man-pages/man1/python3.1.html)

## Learning Objectives

### General Objectives

1. **Why Python programming is awesome**: Python is a powerful and accessible language that can solve a wide range of problems in an elegant and readable way.
2. **How to import functions from another file**: You'll learn to split your code into multiple files to keep it organized and reusable.
3. **How to use imported functions**: Once you've imported a function, you'll learn how to use it within your code.
4. **How to create a Python module**: A module is simply a file containing Python code, and you'll learn how to create and use them.
5. **Using the built-in `dir()` function**: The `dir()` function allows you to list the attributes and methods of an object in Python.
6. **How to prevent code execution when imported**: You'll learn to use `if __name__ == "__main__":` to prevent certain code from executing when a file is imported.
7. **How to use command-line arguments**: You'll discover how to retrieve arguments passed to the program via the command line.

## Requirements

### General Requirements

- Allowed editors: vi, vim, emacs.
- Your code will be interpreted/compiled on Ubuntu 22.04 LTS using Python 3 (version 3.10.*).
- All files must end with a new line.
- The first line of all your files should be exactly `#!/usr/bin/python3`.
- A README.md file at the root of the project directory is mandatory.
- Your code should follow [Pycodestyle](https://www.python.org/dev/peps/pep-0008/) (version 2.7.*).
- All files must be executable.
- The length of your files will be tested using `wc`.

### Useful Commands

Here are a few useful commands for testing or running your Python files:

- Run a Python script: `python3 script_name.py`
- Check the length of a file: `wc -l script_name.py`
- Make a file executable: `chmod +x script_name.py`
- Check the code style (Pycodestyle): `pycodestyle script_name.py`

## Example Usage

Suppose you have a Python file with an `add()` function inside a module. Here's how you can use it:

**File: `math_operations.py`**

```python
#!/usr/bin/python3

def add(a, b):
    return a + b
