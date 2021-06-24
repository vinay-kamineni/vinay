a=['g','i','t','a','m']
res=[]
for i in a:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        res.append(i.capitalize())
    else:
        res.append(i)
print(res)
