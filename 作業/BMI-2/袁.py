bmi_list = []
h_list = []
w_list = []
N = int(input("請輸入你想計算幾份資料"))
for i in range(N): 
    H = float(input("請輸入身高(cm):"))
    W = float(input("請輸入體重(kg):"))
    BMI = round((W/(H*0.01)**2),3)
    h_list.append(H)
    w_list.append(W)
    bmi_list.append(BMI)
print("計算結果：")
print("計算人數：",N,"人")
for a in zip(h_list,w_list):
        print("身高與體重：",a)
print("計算出的bmi值:",bmi_list)
