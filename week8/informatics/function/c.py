def xor(a, b):
    return (a & ~b) | (~a & b)
print(xor(0, 1))