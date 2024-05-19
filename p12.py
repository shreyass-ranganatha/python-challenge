# http://www.pythonchallenge.com/pc/return/evil.html
# http://www.pythonchallenge.com/pc/return/disproportional.html


import ctx


with open(ctx.getstatic(12, "evil2.gfx"), 'rb') as f:
    dt = f.read()


for x in range(0, 5):
    with open(ctx.getstatic(12, "{}.jpeg".format(x)), 'wb') as f:
        f.write(dt[x:len(dt):5])
