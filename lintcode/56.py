numbers=[15, 2, 7, 11]
target=9
l=len(numbers)
flag=0
for i in range(l):
    for j in range(l):
        if i!=j and target==numbers[i]+numbers[j]:
            print([i, j])
            flag=1
            break
    if flag:
        break
