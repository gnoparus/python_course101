def max(a, b, c):
    if a >= b and b >= c:
        return a
    elif b >= a and a >= c:
        return b
    elif c >= a and c >= b:
        return c


print(max(4, 5, 6))
print(max(-5, 5, -10))
print(max(0.5, 15, 33))
