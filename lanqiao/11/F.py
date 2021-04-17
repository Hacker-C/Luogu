n = int(input())
n1 = 0
n2 = 0
for i in range(n):
    x = int(input())
    if x>=60:
        n1+=1
    if x>=85:
        n2+=1
print("{:.0f}".format(n1/n*100))
print("{:.0f}".format(n2/n*100))
