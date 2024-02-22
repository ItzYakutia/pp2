import re


with open("Lab5/row.txt", "r") as f:
    data = f.read()

#lst = []  

#for k in range(0, 50):
    #lst.append("a" + "b" * k)
    
pattern = r'/w*ab*/w*'

a = re.findall(pattern, data)
print(a)
    

