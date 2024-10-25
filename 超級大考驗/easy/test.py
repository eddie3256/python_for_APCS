x=int(input())
a=False #是否為合數
if x==1:
    print("非質數也非合數")
else:
    for i in range(2,x):
        if x%i==0:
            a=True
    if a==False:
        print("質數")
    else:
        print("合數")
