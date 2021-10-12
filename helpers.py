import os
import pickle
from math import *

def sload(fname, find_fun, *args, **kwargs):
    """
    Safe load
    Loads an object from pickle file if it exists.
    Uses find_fun to find this object otherwise.
    Saves object when found.
    """
    if not os.path.isdir("output/"):
        print("Attempting to create output directory automatically!")
        os.mkdir("output")
    if os.path.isfile("output/"+fname):
        with open("output/"+fname, "rb") as f:
            r = pickle.load(f)
    else:
        r = find_fun(*args,**kwargs)
        with open("output/"+fname, "wb+") as f:
            pickle.dump(r,f)
    return r

def is_sg(n: int): # sg for Sophie Germain primes
    return is_prime(2*n + 1)

def is_safe(n: int):
    return is_prime((n-1) // 2) and is_prime(n)

def is_prime(n: int):
    for i in range(2,ceil(sqrt(n)),1):
        if n%i == 0:
            return False
    return True