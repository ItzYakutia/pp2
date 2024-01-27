def Fahrenheit(CentrigradeTemp):
    return ((9 * CentrigradeTemp) / 5) + 32

toFahr = int(input())
print(Fahrenheit(toFahr))