def f(s):
    res = 0
    for i in range(len(s)-1):
        for j in range(i+1, len(s)):
           res += abs(ord(s[i])-ord(s[j]))
    return res
print(f("LANQIAO"))
# 162
