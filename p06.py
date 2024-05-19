# http://www.pythonchallenge.com/pc/def/channel.html
# http://www.pythonchallenge.com/pc/def/oxygen.html

# channel > oxygen

nothings = "static/p06/channel/{}.txt"

n = ["90052"]
for i in range(1000):
    with open(nothings.format(n[-1])) as f:
        rw = f.read()
        if not (tx := rw.split(' ')[-1]).isnumeric():
            break

        n.append(tx)


import zipfile

zip = "static/p06/channel.zip"

with zipfile.ZipFile(zip) as zf:
    dt = {
        x.filename: x for x in zf.infolist()
    }

    for x in n:
        print(dt["{}.txt".format(x)].comment.decode("utf8"), end='')
