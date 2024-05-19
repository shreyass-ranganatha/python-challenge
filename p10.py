# http://www.pythonchallenge.com/pc/return/bull.html
# http://www.pythonchallenge.com/pc/return/5808.html


def groups(N):
    rs = ['']

    pr = N[0]
    for n in N:
        if n == pr:
            rs[-1] += n

        else:
            pr = n
            rs.append(n)
    return rs

def tonumber(sq):
    rs = ""

    for x in sq:
        rs += "{}{}".format(len(x), x[0])

    return rs

a = [1, 11, 21, 1211, 111221, ]
a = [str(x) for x in a]


rs = ["1"]
for i in range(40):
    rs.append(tonumber(groups(rs[-1])))

# print(rs)
print(len(rs[30]))
