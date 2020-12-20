n = int(input())
files = []

for i in range(n):
    s = input().split()
    if len(s) == 2:
        if s[0] == 'touch' and s[1] not in files:
            files.append(s[1])
        if s[0] == 'rm' and s[1] in files:
            files.remove(s[1])
    elif s[0] == 'ls':
        if files:
            for file in files:
                print(file)
    elif len(s) == 3:
        if s[1] in files and s[2] not in files:
            files[files.index(s[1])] = s[2]
    else:
        continue