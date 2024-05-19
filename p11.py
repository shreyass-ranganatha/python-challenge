# http://www.pythonchallenge.com/pc/return/5808.html
# http://www.pythonchallenge.com/pc/return/evil.html


from PIL import Image
import numpy as np

import ctx

with Image.open(ctx.getstatic(11, "cave.jpg")) as f:
    w, h = f.size
    dt = np.array(f.getdata()).reshape((h, w, 3))


odd = dt[0::2,0::2]
Image.fromarray(odd.astype(np.uint8)).save(ctx.getstatic(11, "cave-odd.jpg"))
