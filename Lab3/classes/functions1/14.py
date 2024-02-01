def rev(x):
    st = str(x)
    return(st[::-1])
    
    
print(rev("qwerty"))

def isPrime(x):
    k = 1
    while k < int(x ** 0.5 + 1):
        k += 1
        if (x % k == 0) and x > 2: return False
    if x > 2: return True

#listsepbyspaces = str(input())
listepbyspaces = "1 17 19 49 51 77 97"
lst = listepbyspaces.split()

for k in lst:
    if isPrime(int(k)):
        print(k)
        
        
def GramsToOunce(grams):
    return grams / 28.34952315 # convert to ounces
#a = int(input())
a = 50
print(GramsToOunce(a))