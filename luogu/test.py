# 方法一
def PowerSetsBinary(items):
    N = len(items)
    for i in range(2 ** N):  # 子集个数，每循环一次一个子集
        combo = []
        for j in range(N):  # 用来判断二进制下标为j的位置数是否为1
            if (i >> j) % 2:
                combo.append(items[j])
        print(combo)


PowerSetsBinary([10, 2, 3,4])