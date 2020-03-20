def pw(a,b):
    result = 1
    while b>0:
        result *=a
        b= b-1
    return result
print(pw(2,2))