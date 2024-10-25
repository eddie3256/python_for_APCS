a=float(input("請輸入身高(cm):"))
b=float(input("請輸入體重(kg):"))
c=b/((a/100)**2)
print("您的BMI為%.2f"%c)
if c<18.5:
    print("您的體重為過輕")
elif c<24 and c>=18.5:
    print("您的體重為正常")
elif c<27 and c>=24:
    print("您的體重為過種")
elif c<30 and c>=27:
    print("您的體重為輕度肥胖")
elif c<35 and c>=30:
    print("您的體重為中度肥胖")
else:
    print("您的體重為重度肥胖")
