# http://www.pythonchallenge.com/pc/def/oxygen.html
# http://www.pythonchallenge.com/pc/def/integrity.html

from PIL import Image
import numpy as np


# read PNG
with Image.open("static/p07/oxygen.png") as f:
    w, h = f.size
    dt = np.array(list(f.getdata())).reshape((h, w, 4))

rw = ""
for i in range(0, len(dt[45]), 7):
    px = dt[45][i]

    if not px[0] == px[1] == px[2]:
        break
    rw += chr(px[0])

print(rw)


ar = np.array([105, 110, 116, 101, 103, 114, 105, 116, 121])
print([chr(x) for x in ar])
