def max(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    elif c >= a and c >= b:
        return c


print(max(4, 5, 6))
print(max(-5, 5, -10))
print(max(0.5, 15, 33))
print(max(55, 33, 44))
