import os

p1 = "/Users/yxk/yesyep/lab6/dir/4.txt"
p2 = "/Users/yxk/yesyep/lab6/dir/7.txt"

f = open(p1, "r")

with open(p2, "w") as k:
    for x in f:
        k.write(x)
    
