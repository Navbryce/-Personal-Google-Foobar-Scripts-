def answer(x, y):
    if len(x) > len(y):
        targetSet = set(x)
        otherSet = set(y)
    else:
        targetSet = set(y)
        otherSet = set(x)
    difference = targetSet - otherSet
    return difference.pop()

a = [2]
b = [1, 2]

print(answer(a, b))
