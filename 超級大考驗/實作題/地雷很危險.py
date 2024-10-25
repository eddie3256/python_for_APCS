n, m = map(int, input().split())
x = []
for i in range(n):
    x.append(list(map(int, input().split())))
p = [[0 for i in range(m)] for i in range(n)]
for i in range(n):
    for j in range(m):
        if x[i][j] == 1:
            p[i][j] += 1
            if i + 1 < n:
                p[i+1][j] += 1
            if j + 1 < m:
                p[i][j+1] += 1
            if i - 1 >= 0:
                p[i-1][j] += 1
            if j - 1 >= 0:
                p[i][j-1] += 1
        if x[i][j] == 2:
            for k in range(n):
                p[k][j] += 1
            for l in range(m):
                p[i][l] += 1
            p[i][j] -= 1
for i in p:
    for j in i:
        print(j, end=" ")
    print()
