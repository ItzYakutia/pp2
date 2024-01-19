a = [6, 9, 21]
a1, a2 = 0, 1
while True:
    a.sort()
    k = False
    for i in range(1, len(a)):
        if a[i] > 0 and a[i] > a[i - 1]:
            a[i] -= a[i-1] 
            
            
            k = True  
    if not k:
        break
print(sum(a))
#yes yes