temp={
            'a':1,
            'b':5,
            'c':10,
            'd':50,
            'e':100,
            'f':500,
            'g':1000,
            'h':4,
            'i':9,
            'j':40,
            'k':90,
            'l':400,
            'm':900
        }
baseKeys=['I','V','X','L','C','D','M','IV','IX','XL','XC','CD','CM']
tempKeys=['a','b','c','d','e','f','g','h','i','j','k','l','m']
ans=0
s=input()
for i in range(12, -1, -1):
    s=s.replace(baseKeys[i], tempKeys[i])
for i in s:
    ans+=temp[i]
print(ans)
