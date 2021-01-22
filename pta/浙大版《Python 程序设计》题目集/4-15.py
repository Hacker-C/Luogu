m=int(input())
count=0
for fen5 in range(19, 0,-1):
    for fen2 in range(49,0,-1):
        fen1=m-5*fen5-2*fen2
        if 5*fen5+2*fen2+fen1==m and fen1>0:
            print("fen5:{}, fen2:{}, fen1:{}, total:{}"
                  .format(fen5,fen2,fen1,fen5+fen2+fen1))
            count+=1
print("count={}".format(count))
