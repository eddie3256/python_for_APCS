體重=float(input("請輸入你的體重:"))
身高=float(input("請輸入你的身高:"))
身高=身高/100
BMI=float(體重/身高**2)


if BMI >= 35:
   print("重度肥胖")
elif BMI >= 30:
   print("中度肥胖")
elif BMI >= 27:
   print("輕度肥胖")
elif BMI >= 24:
   print("過重")
elif BMI >= 18.5:
   print("正常")
elif BMI < 18.5:
   print("過輕")
