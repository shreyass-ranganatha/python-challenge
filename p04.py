# http://www.pythonchallenge.com/pc/def/linkedlist.php
# http://www.pythonchallenge.com/pc/def/peak.html

from urllib import request

U = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={}"
n = "12345"

for i in range(400):
    print(i, n)

    with request.urlopen(U.format(n)) as rq:
        n = rq.read().decode("utf8").split(' ')[-1]
