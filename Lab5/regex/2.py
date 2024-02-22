import re


with open("Lab5/row.txt", "r") as f:
    data = f.read()
    
pattern = r'\w*a{1}b{2,3}\w*'

a = re.findall(pattern, data)
print(a)
    

