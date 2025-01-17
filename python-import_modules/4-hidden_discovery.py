#!/usr/bin/python3
import types
import sys
import importlib.util

def get_names_from_pyc(pyc_file):
    # Load the .pyc file using importlib
    spec = importlib.util.spec_from_file_location("hidden_4", pyc_file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    names = dir(module)

    filtered_names = [name for name in names if not name.startswith('__')]

    filtered_names.sort()
    
    return filtered_names

if __name__ == "__main__":
    pyc_file = '/tmp/hidden_4.pyc'
    
    names = get_names_from_pyc(pyc_file)

    for name in names:
        print(name)
