H, W, N = map(int, input().split())

paper = [[0 for i in range(W)] for i in range(H)]

for i in range(N):
    r, c, t, x = map(int, input().split())
    paper[r][c] += x
    for i in range(1, t+1):
        if c+i < W:
            paper[r][c+i] += x
        if c-i > -1:
            paper[r][c-i] += x
        if r+i < H:
            paper[r+i][c] += x
        if r-i > -1:
            paper[r-i][c] += x
    for i in range(1, t+1):
        for j in range(1, t-i+1):
            if r+i < H and c+j < W:
                paper[r+i][c+j] += x
            if r-i > -1 and c-j > -1:
                paper[r-i][c-j] += x
            if r+i < H and c-j > -1:
                paper[r+i][c-j] += x
            if r-i > -1 and c+j < W:
                paper[r-i][c+j] += x

for i in paper:
    for j in i:
        print(j, end = " ")
    print()
