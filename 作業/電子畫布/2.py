H, W, N = list(map(int, input().split()))
畫布= [[0]*W for _ in range (H)]

for _ in range(N):
    r, c, t, x = list(map(int, input().split()))
    for i in range(H):
        for j in range(W):
            if abs(i - r) + abs(j - c) <= t:
                畫布[i][j]+=x

for 列表 in 畫布:
    print(' '.join(map(str, 列表)))
