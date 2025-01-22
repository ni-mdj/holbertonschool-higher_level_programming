# Python Lists and Tuples Project

## Project Description

This project focuses on understanding and mastering **lists** and **tuples** in Python. By the end of this project, you will be able to create, modify, and manipulate lists and tuples using various Python methods and operations. You will also learn when to use each of these data structures.

## Learning Objectives

By the end of this project, you should be able to explain the following concepts:

### General Concepts:
- **Lists**:
  - What is a list and how to use it in Python?
  - What are the differences and similarities between lists and strings?
  - What are the most common methods of lists and how to use them?
  - How to use lists as stacks (LIFO) and queues (FIFO)?

- **List Comprehensions**:
  - What are list comprehensions and how to use them for more concise code?

- **Tuples**:
  - What is a tuple and how to use it?
  - When should you use a tuple instead of a list?
  - What is **tuple packing** and **tuple unpacking**?

- **Sequences**:
  - What is a sequence in Python and how do you work with it?
  - How to use the `del` statement to delete elements in lists and tuples?

### Methods and Operations:
- Manipulate lists and tuples using common methods like `append()`, `remove()`, `insert()`, `pop()`, etc.
- Use the `del` statement to remove elements from a sequence.
- Work with **tuple packing** and **unpacking**.

## Requirements

- **Python version**: Your code should be compatible with Python 3.8.5 or higher.
- **Text Editors**: Allowed editors include vi, vim, emacs.
- **Operating System**: Code should run on Ubuntu 20.04 LTS.
- **Executable files**: All scripts should be executable.
- **First line of scripts**: All Python scripts must start with `#!/usr/bin/python3`.
- **Code Style**: Your code must adhere to the **pycodestyle** standard (version 2.7.*).
- **File Structure**: A `README.md` file must be included at the root of your project directory.

## Example Code (C)

In this example, we'll simulate Python lists and tuples using C arrays and structs.

```c
#include <stdio.h>
#include <stdlib.h>

// Define a tuple-like struct
typedef struct {
    int a;
    int b;
    int c;
} Tuple;

// Function to print the tuple
void print_tuple(Tuple t) {
    printf("Tuple values: %d, %d, %d\n", t.a, t.b, t.c);
}

int main() {
    // Simulate a Python list with an array
    int list[] = {1, 2, 3, 4, 5};
    int list_size = sizeof(list) / sizeof(list[0]);

    // Add an element to the list (simulated by resizing the array)
    list_size++;
    list = realloc(list, list_size * sizeof(int));
    list[list_size - 1] = 6;

    // Print the modified list
    printf("Modified list: ");
    for (int i = 0; i < list_size; i++) {
        printf("%d ", list[i]);
    }
    printf("\n");

    // Create a tuple (struct)
    Tuple t = {10, 20, 30};
    print_tuple(t);

    // Simulate tuple unpacking
    int a = t.a, b = t.b, c = t.c;
    printf("Unpacked values: %d, %d, %d\n", a, b, c);

    // Free allocated memory
    free(list);

    return 0;
}
