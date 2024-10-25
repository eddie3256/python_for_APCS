N, Q = list(map(int, input().split()))

NA = list(map(int, input().split()))
minus = []
for i in range(len(NA)):
    for j in range(i+1, len(NA)):
        minus.append(abs(NA[i] - NA[j]))
        #minus.append(N[i] - N[j] if N[i] - N[j] > 0 else N[j] - N[i])

for i in range(Q):
    print("YES" if int(input()) in minus else "NO")
