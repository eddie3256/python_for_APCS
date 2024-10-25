print("BMI計算器")
h = float(input("請輸入你的身高(m)："))
while h <= 0.4:
    print("你是認真的嗎？")
    h = float(input("請輸入你的身高(m)："))
    if h > 0.4:
        break 
w = float(input("請輸入你的體重(kg)："))
while w <= 2:
    print("你是認真的嗎？")
    w = float(input("請輸入你的體重："))
    if w > 2:
        break 
BMI = float(w / h**2)
if BMI < 18.5:
    print("你的BMI指數是:",BMI,"體重過輕")
elif BMI <24:
    print("你的BMI指數是:",BMI,"正常")
elif BMI <27:
    print("你的BMI指數是:",BMI,"體重過重")
elif BMI <30:
    print("你的BMI指數是:",BMI,"輕度肥胖")
elif BMI <35:
    print("你的BMI指數是:",BMI,"中度肥胖")
else:
    print("你的BMI指數是:",BMI,"重度肥胖")