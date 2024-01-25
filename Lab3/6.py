lst = [1, 3, 21, 17, 44, 65, 5]
new = filter(lambda k: all(k % x for x in range(2, int(k ** 0.5)+1)) and k > 2, lst)
print(list(new))




