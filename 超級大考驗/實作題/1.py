def 質數(n):
    if n == 1:
        return 0
    else:
        if n % 2 == 0 and n != 2:
            return 0
        else:
            if n % 3 == 0 and n != 3:
                return 0
            else:
                for i in range(5, int(n**0.5)+1, 6):
                    if n % i == 0:
                        return 0
                    if n % (i+2) == 0: 
                        return 0            
    return 1        
while True:
    try:
        a, b = list(map(int, input().split()))        
        if b - a > 1000:
            print(0)
            break        
        數量 = 0
        for i in range(a, b+1):
            數量+= 質數(i)                
        print(數量)        
    except:
        break
