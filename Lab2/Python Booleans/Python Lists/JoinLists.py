lis1 = ["marvel", "georgeous", "flow"]
lis2 = [1, 2, 3]
print(lis1 + lis2)

for x in lis1:
    lis2.append(x)
print(lis2)

lis3 = ["marvel", "georgeous", "flow"]
lis4 = [1, 2, 3]
lis3.extend(lis4)
print(lis3)