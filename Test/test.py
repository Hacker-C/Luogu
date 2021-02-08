from itertools import chain


def spread(ls):
    ans = []
    for i in ls:
        if isinstance(i, list):
            return spread(i)
        else:
            ans.append(i)
    return ans


def spread(lst, res=None):
    if res is None:
        res = []
    for item in lst:
        if isinstance(item, list):
            spread(item, res)
        else:
            res.append(item)
    return res


def spred2(lst):
    res = []
    while lst:
        head = lst.pop(0)
        if isinstance(head, list):
            lst = head + lst
        else:
            res.append(head)
    return res


inputlist = ['it', 'is', ['a', ['test', 'of', ['circle', 'lists'], ','], 'please', 'like', ['it', 'and'], 'hello'], 'world']


lst = [1, [2, 3], [[4, [5, 6]], 7], [8, 9], 10]
print(spread(lst))
# print(spread(lst))
print(flat2(inputlist))
