def multlist(lis):
    res = 1
    for x in lis:
        res *= x
    return res

ls = [1, 2, 3, 4, 5]

print(multlist(ls))