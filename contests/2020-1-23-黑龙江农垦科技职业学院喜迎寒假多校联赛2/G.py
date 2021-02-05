n=int(input())
ans=0
for i in range(n):
    s=input()
    s=s.replace(' ','')
    if 'Alan' in s:
        ans+=s.count('%')
print(ans)
