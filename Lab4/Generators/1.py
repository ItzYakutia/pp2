def nGEN(N):
    for i in range(1, N):
        yield i ** 2

for k in nGEN(16):
    print(k)