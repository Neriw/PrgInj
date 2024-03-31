a = [2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4]
b = [4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4]
c = [5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4]
acorect = []
bcorect = []
ccorect = []
for i in range(len(a)):
    if a[i]==3:
        acorect.append(a[i]+1)
    elif a[i]!=2:
        acorect.append(a[i])
a=acorect
for i in range(len(b)):
    if b[i]==3:
        bcorect.append(b[i]+1)
    elif b[i]!=2:
        bcorect.append(b[i])
b=bcorect
for i in range(len(c)):
    if c[i]==3:
        ccorect.append(c[i]+1)
    elif c[i]!=2:
        ccorect.append(c[i])
c=ccorect
print(f"{a}\n{b}\n{c}")
