#!/usr/bin/python3

from sys import stderr

def safe_function(fct, *args):
    result = None
    error = None
    
    try:
        result = fct(*args)
    except Exception as err:
        error = err
    
    if error is not None:
        print('Exception: {}'.format(error), file=stderr)
    
    return result
