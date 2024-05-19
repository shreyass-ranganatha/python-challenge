
import os
import sys


def getstatic(p: int, f: str):
    pt = os.path.join(os.path.dirname(__file__), "static", "p{}".format(p))

    if not os.path.exists(pt) and not os.path.isdir(pt):
        os.makedirs(pt)

    return os.path.join(pt, f)
