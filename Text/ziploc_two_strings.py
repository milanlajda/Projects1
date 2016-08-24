def ziploc():
    a = "abcdefgh"
    b = "12345678"
    c = []
    if len(a) >= len(b):
        for x in range (0, len(a)):
            c.append(a[x])
            c.append(b[x])

    else:
        for x in range (0, len(b)):
            c.append(a[x])
            c.append(b[x])

    print c

ziploc()

