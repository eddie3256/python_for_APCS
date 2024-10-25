while True:
    try:
        a, b = map(int, input().split())
        nums = [i for i in range(a, b+1)]
        nums = list(filter(lambda x: (x > 1) and (x % 2 or x == 2) and (x % 3 or x == 3), nums))
        for i in range(5, int(b ** 0.5) + 1, 6):
            nums = list(filter(lambda x: (x % i or x == i) and (x % (i + 2) or x == (i + 2)), nums))
        print(len(nums))
    except:
        break
