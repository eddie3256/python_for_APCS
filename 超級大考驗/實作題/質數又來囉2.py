def f(i):
    if i <= 1:
        return 0
    elif i % 2 == 0 and i != 2:
        return 0
    elif i % 3 == 0 and i != 3:
        return 0
    else:
        for j in range(5, int(i ** 0.5) + 1, 6):
            if i % j == 0 or i % (j+2) == 0:
                return 0
        else:
            return 1

while True:
    try:
        a, b = map(int, input().split())
        x = 0
        for i in range(a, b+1):
            x += f(i)
        print(x)
    except:
        break
