import re


with open("Lab5/row.txt", "r") as f:
    data = f.read()
    
pattern = r'\b[a-z]+_[a-z]+\b'

a = re.findall(pattern, data)
print(a)
    

