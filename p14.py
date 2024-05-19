# http://www.pythonchallenge.com/pc/return/italy.html
#


import ctx
from PIL import Image
import numpy as np
import math

with Image.open(ctx.getstatic(14, "wire.png")) as f:
    w, h = f.size
    dt = list(f.getdata())


# S = 0
# a, b = 0, 1

# for i in range(1000):
#     if S >= 100_00:
#         print(i)
#         break

#     S += math.fabs(100 - a)
#     a, b = b, a+b

# print(S)




ar = [
    [] for x in range(100)
]

try:
    a, b = 0, 1
    for i, x in enumerate(dt):
        ar[i//100].append(x)

        a, b = b, a+b
finally:
    pass


rs = []

Image.fromarray(np.array(ar, dtype=np.uint8)).save(ctx.getstatic(14, "result.png"))
