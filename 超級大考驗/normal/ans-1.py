p, g, b, m, c = list(map(int, input().split()))

hit = 900000/(p+g+b+m)

hitS = p * hit + g * hit * 0.8 + b * hit * 0.5

cS = c/(p+g+b+m) * 100000

total = round(hitS + cS)
print(total)
