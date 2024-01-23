thistuple = ("banana", "orange", "pineapple", "pineapple2", "PPAP")
y = list(thistuple)
y[1] = "green"
y.append("applepan")
thistuple = tuple(y)
print(thistuple)

newtu = ("mango",)
thistuple += newtu
print(thistuple)

y2 = list(thistuple)
y2.remove("PPAP")
newtuple = tuple(y2)
print(newtuple)

del newtuple


