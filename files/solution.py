def solve(fil):
    a = open(fil, 'rb')
    b = a.read()
    c = b[::-1]
    return c
