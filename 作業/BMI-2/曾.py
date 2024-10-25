a=int(input())
listt=[]
for i in range(a):
    b,c=map(int,input().split())
    d=c/((b/100)**2)
    listt.append(d)
for i in range(a):
    print('%.2f'%listt[i],end=' ')