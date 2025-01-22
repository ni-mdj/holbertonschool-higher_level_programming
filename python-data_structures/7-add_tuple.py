#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    # Extend tuples to at least 2 elements, filling with 0s if necessary
    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)
    
    # Sum the first two elements of each tuple
    return (a[0] + b[0], a[1] + b[1])
