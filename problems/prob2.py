def test(x, y=5,z=None):
    if z is None:
        z = []
    z.append(x+y)
    return z

print(test(1), test(2))
