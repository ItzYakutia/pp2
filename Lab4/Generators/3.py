def iter(k):
    for x in range(1, k):
        if x % 3 == 0 and x % 4 == 0:
            yield x

n = int(input())
for x in iter(n):
    print(x)
