def getValue(x, y):
    if 0 <= y <= x:
        if y == 0 or x == y:
            return 1
        return getValue(x - 1, y - 1) + getValue(x - 1, y)
    return -1


print(getValue(3, 2))
