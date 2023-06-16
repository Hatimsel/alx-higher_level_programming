#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_dict = a_dictionary.copy()
    keys_to_delete = []

    for key in new_dict:
        if new_dict[key] == value:
            keys_to_delete.append(key)
    for key in keys_to_delete:
        del new_dict[key]
    return new_dict
