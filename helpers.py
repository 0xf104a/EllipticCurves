import os
import pickle

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