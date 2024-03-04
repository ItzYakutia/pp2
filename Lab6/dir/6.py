import os

dir = "/Users/yxk/yesyep/lab6/dir/6AZ"
os.makedirs(dir, exist_ok=True)

for x in range(65, 91):
    fN = f"{chr(x)}.txt"
    fP = os.path.join(dir, fN)
    with open(fP, "w") as f:
        f.write(chr(x))


