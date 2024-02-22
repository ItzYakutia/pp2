import re


with open("Lab5/row.txt", "r") as f:
    data = f.read()
    
pattern = r'\b[A-Z][a-z]+\b'

a = re.findall(pattern, data)
print(a)
    

