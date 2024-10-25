N=int(input("有幾個人:"))
BMIS=[]
for BMI in range(N):
    H, W=input("H(cm), W(kg):").split()
    W=float(W)
    H=float(H)
    H=H/100
    BMI=float(W/H**2)

    BMIS.append(round(BMI, 3))
print(BMIS)
