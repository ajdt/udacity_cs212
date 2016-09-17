def ints(start, end = None):
    i = start
    while i <= end or end is None:
        yield i
        i = i + 1


def all_ints():
    "Generate integers in the order 0, +1, -1, +2, -2, +3, -3, ..."
    function = ints(0)
    i = function.next()

    while True :
        yield i
        if (i*-1) < i : # i is positive
            i *= -1
        else:
            i = function.next()


f = all_ints()
for i in range(0, 10):
    print f.next(), " "
