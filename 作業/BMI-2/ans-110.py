n = int(input())
datas = []
for i in range(n):
    data = input().split()
    datas.append(data)

BMIs = []
for data in datas:
    h = float(data[0]) / 100
    w = float(data[1])
    BMI = w / h ** 2
    BMIs.append(BMI)

for BMI in BMIs:
    print(round(BMI, 2), end=" ")


"""
1
160 50
19.53

5
200 100
160 50
153 38
155 45
170 53
25.0 19.53 16.23 18.73 18.34
"""
