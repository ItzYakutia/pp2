import os

def c_lines(ss):
    if os.path.exists(ss):
        with open(ss, "r") as f:
            k = 0
            for l in f:
                k += 1
        return k
    else:
        print("For what u doing it")

pa = "/Users/yxk/yesyep/lab6/dir/4.txt"
print(c_lines(pa))