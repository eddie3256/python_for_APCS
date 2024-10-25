#test
while True:
    try:
        n = int(input())
        if n > 1000 or n < 1:
            raise TypeError
        break
    except:
        pass

if n <= 10:
    print("普通")
elif n <= 50:
    print("常見")
elif n <= 100:
    print("罕見")
elif n <= 200:
    print("超級稀有")
elif n <= 500:
    print("史詩")
else:
    print("傳說")