import re

def is_camel(s):
    return bool(re.match(r'(^[a-zA-Z]+[A-Z]+)', s))
def camel_to_snake(s):
    return re.sub(r'([A-Z]+)', r'_\1', s).lower()


tex = "TheRainInSpain"
print(is_camel(tex))
if is_camel(tex):
    print(camel_to_snake(tex))