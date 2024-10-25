def DataToBMI(data):
    h = float(data[0]) / 100
    w = float(data[1])
    BMI = w / h ** 2
    return BMI

n = int(input())
datas = []
for i in range(n):
    datas.append(list(map(float, input().split())))

BMIs = []
for data in datas:
    BMIs.append(DataToBMI(data))

for BMI in BMIs:
    print(f"{BMI:.2f}", end=" ")
