def rotate(L):
    L2 = [[0 for i in range(len(L))] for i in range(len(L[0]))]
    for i in range(len(L2)):
        for j in range(len(L2[0])):
            L2[i][j] = L[j][-i-1]
    return L2

def flip(L):
    for i in range(round(len(L)/2)):
        L[i], L[-i-1] = L[-i-1], L[i]
    return L

R, C, M = map(int, input().split())
L = []
for i in range(R):
    L.append(list(map(int, input().split())))
M = list(map(int, input().split()))[::-1]
for i in M:
    if i == 0:
        L = rotate(L)
    if i == 1:
        L = flip(L)
print(len(L), len(L[0]))
for i in L:
    for j in i:
        print(j, end=" ")
    print()
