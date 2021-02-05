# 超时代码
n, m = map(int, input().split())
ls = [0 for i in range(n+1)]
ls[1:] = map(int, input().split())
lists = []
ans=0
for i in range(m):
    st = set(map(int, input().split()))
    flag = 1
    for j in range(len(lists)):
        if (a:=st&lists[j]):
            lists[j] = lists[j] | st
            flag=0
            break
    if flag:
        lists.append(st)
print(lists)
SET = set(i+1 for i in range(n))
print(SET)
#并集
t = set()
for set_elem in lists:
    mx = 0
    for j in list(set_elem):
        if ls[j] > mx:
            mx = ls[j]
    ans += len(set_elem) * mx
    t = t | set_elem
#差集
p = SET - t
for i in p:
    ans += ls[i]
print(ans)
        
    
