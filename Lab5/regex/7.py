import re

def is_snake_case(s):
    return bool(re.match(r'^[a-z]+(?:_[a-z]+)*$', s))
def snake_to_camel(s):
    return re.sub(r'_([a-z])', lambda x: x.group(1).upper(), s)

lst = []
with open("Lab5/row.txt", "r") as f:
    for line in f:
        words = line.split()
        for x in words:
            if is_snake_case(x):
                x = snake_to_camel(x)
            print(x)


    
    



                



