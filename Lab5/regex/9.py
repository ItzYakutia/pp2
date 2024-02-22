import re

def spaces(s):
    res = re.sub(r'([A-Z]+)', r' \1', s)
    return res

text = "TheRainInSpain"
print(spaces(text))