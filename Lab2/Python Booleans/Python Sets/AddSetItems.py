newset = {"unique", "unrepeated", "yes"}
newset.add("newunique")
print(newset)

anotherset = {1, 2, 3}

newset.update(anotherset)
print(newset)

lis = list((5, 6, 7))

newset.update(lis)
print(newset)
print(type(newset))