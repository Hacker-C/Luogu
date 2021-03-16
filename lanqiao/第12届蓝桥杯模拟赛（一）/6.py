l = int(input())
h = int(input())
ans = h * l / 2
if int(ans) == ans:
    print(int(ans))
else:
    print(round(ans, 1))
