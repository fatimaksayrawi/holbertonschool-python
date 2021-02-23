#!/usr/bin/python3
<<<<<<< HEAD
"""to json and write in a file"""

=======

"""
save_to_json_file Module
"""
>>>>>>> bf9c53e24777c19bf9f0689a7ec9f169dcef6d3f

import json


def save_to_json_file(my_obj, filename):
<<<<<<< HEAD
    """ Returns an object python
        it could also be said that it converts from JSON to python
    """
    with open(filename, "w") as writer:
        writer.write(json.dumps(my_obj))
=======
    """Writes an Object to the text file by using JSON"""
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
>>>>>>> bf9c53e24777c19bf9f0689a7ec9f169dcef6d3f
