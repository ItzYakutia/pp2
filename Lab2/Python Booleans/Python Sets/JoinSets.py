newset = {"unique", "unrepeated", "yes"}
anotherset = {1, 2, 3, "yes"}
set1 = newset.union(anotherset)
print(set1)
set1.update(anotherset)
print(set1)

newset.intersection_update(anotherset)
print(newset)

newset1 = {"unique", "unrepeated", "yes"}
anotherset1 = {1, 2, 3, "yes"}

xy = newset1.intersection(anotherset1)
print(xy)

newset1.symmetric_difference_update(anotherset1)
print(newset1)

newset2 = {"unique", "unrepeated", "yes"}
anotherset2 = {1, 2, 3, "yes"}
ne = newset2.symmetric_difference(anotherset2)
print(ne)