s = list(input().strip('\n\r'))
if '.' in s:
    s.remove('.')
s = ''.join(s).lower().split()

ls = []


def f(num):
    if len(str(num)) == 1:
        return '0' + str(num)
    else:
        return str(num)


dct = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'ten': 10,
    'eleven': 11,
    'twelve': 12,
    'thirteen': 13,
    'fourteen': 14,
    'fifteen': 15,
    'sixteen': 16,
    'seventeen': 17,
    'eighteen': 18,
    'nineteen': 19,
    'twenty': 20,
    'a': 1,
    'both': 2,
    'another': 1,
    'first': 1,
    'second': 2,
    'third': 3
}
flag = 0
for i in s:
    if i in dct.keys():
        flag = 1
        ls.append(f(dct[i] ** 2 % 100))

if flag:
    ls2 = list(map(int, ls))
    ls2.sort()
    ls2 = list(map(f, ls2))
    ans = int(''.join(ls2))
    print(ans)
else:
    print(0)
