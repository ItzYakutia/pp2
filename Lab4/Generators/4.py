def squares(a, b):
    for x in range(a, b):
        yield x ** 2

a = int(input())
b = int(input())

for k in squares(a, b):
    print(k)