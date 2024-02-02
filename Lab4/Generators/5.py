def don(n):
    for x in range(n, -1, -1):
        yield x

a = int(input())
for k in don(a):
    print(k)