N = int(input())
x = []

for i in range(N):
    x.append(list(map(int, input().split())))

x.sort()
L = x[0][0]
R = x[0][1]
ran = []
for l, r in x[1:]:
    if l > R:
        ran.append([L, R])
        L = l
        R = r
    elif r > R:
        R = r
ran.append([L, R])

sum = 0
for l, r in ran:
    sum += r-l

print(sum)
