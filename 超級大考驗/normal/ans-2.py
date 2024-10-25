n = int(input())
times = []
for i in range(n):
    time = list(map(int, input().split()))
    times.append(time)

total = []
acc = []
for i in times:
    hitT = i[0] + i[1] + i[2] + i[3]
    hit = 900000 / hitT
    hitS = i[0] * hit + i[1] * hit * 0.8 + i[2] * hit * 0.5
    cS = i[4] / hitT * 100000
    sum = hitS + cS
    total.append(round(sum))
    a = hitS / 900000 * 100
    acc.append(round(a, 2))
    
for i in total:
    print(i, end=" ")
print()
for i in acc:
    print(i, end=" ")
print()
print(sorted(total)[-1], sorted(acc)[-1])


"""
1
1050 250 30 20 1000

917407 
93.7 
917407 93.7
"""
"""
4
1000 300 100 100 500
725 23 1 1 305
815 105 32 58 145
1465 105 32 6 1033

807333 933347 829703 940174 
86.0 99.19 90.59 97.33 
940174 99.19
"""
