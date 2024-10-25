n = int(input())
x = list(map(int, input().split()))
total = 0
for i in range(1, n+1):
    total += i * x[i-1]

print(total)
