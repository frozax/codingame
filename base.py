import sys
import math

########################################################## HELPER FUNCTIONS
from collections import namedtuple

def dbg(*args):
    print("DBG:", *args, file=sys.stderr)
    
def dbg_var(*args):
    for var_name in args:
        assert type(var_name) == str
        calling_frame = sys._getframe().f_back
        var_val = calling_frame.f_locals.get(var_name, calling_frame.f_globals.get(var_name, None))
        dbg(var_name + '=' + str(var_val))

def french_str_to_float(string):
    return float(string.replace(",", "."))


########################################################## HELPER FUNCTIONS

