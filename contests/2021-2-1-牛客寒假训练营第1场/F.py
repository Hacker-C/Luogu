n = int(input())
ls1 = input().split()
ls2 = input().split()
same = 0
diff = 0
for i in range(n):
    if ls1[i] == ls2[i]:
        same += 1
    else:
        diff += 1
ans1 = same * 2 + diff
ans2 = 0
print(ans1, ans2)
