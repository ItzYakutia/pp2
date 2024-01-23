newset = {"unique", "unrepeated", "yes", 1, 2}
newset.remove("unique")
print(newset)

newset.discard(2)
print(newset)

x = newset.pop()
print(x)

newset.clear()
print(newset)

del newset
print(newset)