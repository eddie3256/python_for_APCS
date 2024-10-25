class x():
    def __init__(self, left, s, right):
        self.L = left
        self.S = s
        self.R = right
    def left(self, all, n, H):
        if n == 0 :
            return 0
        if H > self.L:
            return all[n-1].left(all, n-1, H) + self.L
        return 0
    def right(self, all, n, H):
        if n == len(all)-1 :
            return 0
        if H > self.R:
            return all[n+1].right(all, n+1, H) + self.R
        return 0


n = int(input())
h = list(map(int, input().split()))
m = [None] * n
for i in range(n):
    m[i] = x(h[i-1] if i-1 >= 0 else h[i], h[i], h[i+1] if i+1 < n else h[i])
for i in range(n):
    print(m[i].left(m, i, m[i].S) + m[i].right(m, i, m[i].S))
    
