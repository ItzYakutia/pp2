lis = ["minecraft", "pig", "peppa", "bear"]
lis.sort()
print(lis)

lis1 = [100, 23, 77, 1]
lis1.sort()
print(lis1)

lis12 = [100, 23, 77, 1]
lis12.sort(reverse = True)
print(lis12)

lis3 = [100, 23, 77, 1]
lis3.reverse()
print(lis3)

def func(n):
  return abs(n - 50)

lis2 = [100, 50, 65, 82, 23]
lis2.sort(key = func)
print(lis2)