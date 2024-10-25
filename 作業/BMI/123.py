h = float(input("請輸入你的身高(cm): "))/100
w = float(input("請輸入你的體重(kg): "))

BMI = w / h ** 2

print(round(BMI, 3))

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
else:
   print("過輕")
