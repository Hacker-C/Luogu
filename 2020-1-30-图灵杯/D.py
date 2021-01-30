t=int(input())
for i in range(t):
    n,k=map(int, input().split())
    n-=1
    if n%(k+1):
        print("yo xi no forever!")
    else:
        print("ma la se mi no.1!")
