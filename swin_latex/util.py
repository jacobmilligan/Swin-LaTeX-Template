import os
import sys

def print_error(msg):
    prog_name = os.path.basename(__file__)
    print('{0}: error: {1}', prog_name, msg)
