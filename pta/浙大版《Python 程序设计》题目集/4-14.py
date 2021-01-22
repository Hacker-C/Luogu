txt = ''
while True:
    k = input()
    txt += k + '\n'
    if len(txt) >= 11:
        txt=txt[:-1]
        break
letter,blank,digit,other=0,0,0,0
print(len(txt))
for i in txt:
    try:
        i=int(i)
        digit+=1
    except:
        if 'a'<=i<='z' or 'A'<=i<='Z':
            letter+=1
        elif i==' ' or i=='\n':
            blank+=1
        else:
            other+=1
print("letter = {0}, blank = {1}, digit = {2}, other = {3}"
      .format(letter,blank,digit,other))

            

    
