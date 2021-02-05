distance = float(input())
distance /= 1000
r0 = 11.5 / 2
if distance <= r0:
    print(10)
elif distance <= r0 + 8:
    print(9)
elif distance <= r0 + 16:
    print(8)
elif distance <= r0 + 24:
    print(7)
elif distance <= r0 + 32:
    print(6)
elif distance <= r0 + 40:
    print(5)
elif distance <= r0 + 48:
    print(4)
elif distance <= r0 + 56:
    print(3)
elif distance <= r0 + 64:
    print(2)
elif distance <= r0 + 72:
    print(1)
else:
    print(0)
