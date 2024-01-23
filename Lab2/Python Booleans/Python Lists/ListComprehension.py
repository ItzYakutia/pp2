lis = ["minecraft", "pig", "peppa", "bear"]
newl = [x for x in lis]
print(newl)

newl2 = [x for x in lis if "i" in x]
print(newl2)

newl3 = [x.upper() for x in lis]
print(newl3)