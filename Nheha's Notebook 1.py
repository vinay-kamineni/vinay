a={'b':1,'a':2,'d':4,'c':5}
b={}
for k in a:
    v=a[k]
    if v not in b:
        b[v]=k
    else:
        b[v].append(k)
print(a)
print(b)