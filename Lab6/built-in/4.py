import time, math

def sqroot(i, t):
    time.sleep(t/1000)
    return math.sqrt(i)

i = int(input("Input number: "))
t = int(input("Input time: "))

print(f"Square root of {i} after {t} miliseconds is {sqroot(i, t)}")
    
    