x=input()
a=set(x)
ababab=list(a)
c=0
for i in range(len(ababab)):
    if x.count(f'{ababab[i]}')%2==1:
        c+=1
if c>1:
    print('no')
else:
    print('yes')
