import re

with open("Lab5/row.txt", "r") as f:
    for line in f:
        line = re.sub(r'[ ,.]', ':', line)
        print(line)
                



