while True:
    try:
        a = int(input())
        f = g = 0
        for i in range(1, a+1):
            f += i
            g += f
        print(f, g)
    except:
        break
