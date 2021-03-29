# 方法一 api
#print(len(bin(10000))-2)
# 方法二 10进制转k进制：除k取余法
def change(num, k):
    ls = []
    while num > 0:
        ls.append(num % k)
        num //= k
    _ls = ''.join([str(i) for i in ls[::-1]])
    return _ls
print(len(change(10000, 2)))
        
