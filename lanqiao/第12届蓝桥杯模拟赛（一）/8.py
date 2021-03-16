# 尚存疑惑
w = 'LANQIAO'
w = 'AAB'
t = 1
for i in range(t):
    if w[0] > w[1]:
        w = w.replace(w[0], '', 1)
    else:
        w = w.replace(w[1], '', 1)
print(w)
    
