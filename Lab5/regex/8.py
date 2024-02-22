import re

txt = "The rain in Spain"
x = re.split(r"\s", txt)
for e, k in enumerate(x):
    if ord(k[0]) > 64 and ord(k[0]) < 91:
        None
    else: 
        x[e] = k[0].upper() + k[1:]
            
res = " ".join(x)
        
print(res)