def main():
    n = int(input())
    h = list(map(int, input().split()))
    for i in range(n):
        k, t = 1, 0
        while i-k >= 0 and h[i] > h[i-k]:
            t += h[i-k]
            k += 1
        k = 1
        while i+k < n and h[i] > h[i+k]:
            t += h[i+k]
            k += 1
        print(t)

if __name__ == "__main__":
    main()
