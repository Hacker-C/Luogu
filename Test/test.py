from functools import reduce

nums = [1, 2, 3, 4, 5]
sm = reduce(lambda x, y: x + y, nums)
print(sm)
