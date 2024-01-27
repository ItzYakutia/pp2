def isPrime(x):
    k = 1
    while k < int(x ** 0.5 + 1):
        k += 1
        if (x % k == 0) and x > 2: return False
    if x > 2: return True

listsepbyspaces = str(input())
lst = listsepbyspaces.split()

for k in lst:
    if isPrime(int(k)):
        print(k)