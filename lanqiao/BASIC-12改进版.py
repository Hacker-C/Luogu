n = int(input())
for i in range(n):
    ss = input()
    hx = '0x'+ss
    hx = eval(hx)
    ans = oct(hx)
    print(ans[2:])
