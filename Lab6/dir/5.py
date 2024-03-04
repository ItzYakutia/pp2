import os

l = ["It", "'", "s", "my", "list"]

dir = "/Users/yxk/yesyep/lab6/dir/"
fN = "5FileList5.txt"
fP = os.path.join(dir, fN)

os.makedirs(dir, exist_ok=True)

with open(fP, 'w') as file:
    for item in l:
        file.write(f"{item}\n")

print(f"List has been written to {fP}")
