m = int(input())
d = int(input())
if (m==1 or m==3 or m==5 or m==7 or m==8 or m== 10 or m== 12) and d<=31:
    print('yes')
elif (m==4 or m==6 or m==9 or m==11) and d <= 30:
    print('yes')
elif m == 2 and d <= 28:
    print('yes')
else:
    print('no')
