a = input()
times = {}
for i in a:
    if i in times:
        times[i] += 1
        continue
    times[i] = 1

count = times.values()
mid = False
for i in count:
    if i % 2 == 1:
        if mid == True:
            print("no")
            break
        mid = True
else:
    print("yes")


"""
xxxyyyzz
no

152a3ba3251
yes
"""
