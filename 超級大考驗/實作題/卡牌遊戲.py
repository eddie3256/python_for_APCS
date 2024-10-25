n, k = map(int, input().split())
a = list(map(int, input().split()))

for i in range(k):
    a.sort()
    a[0] *= -1

print(sum(a))
