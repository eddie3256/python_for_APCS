def main():
    n = list(map(int, input().split()))
    n , nums = n[0], n[1:]
    a = 0
    for i in range(n):
        if sum(nums[0:i+1]) == sum(nums[n-i-1:n]):
            a += 1
    print(a)

if __name__ == "__main__":
    main()
