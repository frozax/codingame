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

POS = namedtuple('POS', ["long", "lat"])
DEFIB = namedtuple('DEFIB', ["num", "name", "address", "phone", "long", "lat"])
class DEFIB:
    def __init__(self, num, name, address, phone, long, lat):
        self.name = name
        self.pos = POS(french_str_to_float(long), french_str_to_float(lat))
    def __str__(self):
        return "%s: %s" % (self.name, self.pos)

def compute_dist(A, B):
    """distance between two points
    A, B: 2-tuple with (long,lat)
    """
    x = (B.long - A.long) * math.cos((A.lat + B.lat)/2)
    y = (B.lat - A.lat)
    d = math.sqrt(x*x + y*y) * 6371
    return d


lon = input()
lat = input()
man = POS(french_str_to_float(lon), french_str_to_float(lat))
n = int(input())
best_defib = None
best_dist = -1
for i in range(n):
    defib = DEFIB(*input().split(';'))
    dbg(defib)
    dist = compute_dist(defib.pos, man)
    if best_defib is None or dist < best_dist:
        best_defib = defib
        best_dist = dist

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
dbg(best_defib)
print(best_defib.name)
