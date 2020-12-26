n=int(input())
x = input().split()
name = x[0]
ans = {x[0]: list(map(int, x[1:]))}
temp = {}
for i in range(1, n):
    lst = input().split()
    temp[lst[0]] = list(map(int, lst[1:]))
    if sum(temp[lst[0]]) > sum(ans[x[0]]):
        ans[lst[0]] = lst[1:]
        name = lst[0]
print(name, end=' ')
for i in ans[name]:
    print(i, end=' ')