import re

with open("Lab5/row.txt", "r") as f:
    text = f.read()

words = re.findall(r'\b\w+\b', text)

lst = []
for word in words:
    if word[0] == "a" and word[-1] == "b":
        lst.append(word)
print(lst)
