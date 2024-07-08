score = float(input("請輸入你的成績: "))

if score > 100:
    print("請重新開始程式")
elif score >= 90:
    print("優")
elif score >= 80:
    print("甲")
elif score >= 70:
    print("乙")
elif score >= 60:
    print("丙")
elif score >= 0:
    print("丁")
else:
    print("請重新開始程式")
