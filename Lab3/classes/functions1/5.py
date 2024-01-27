from itertools import permutations

def perm(x):
    s = permutations(x)
    for i in s:
        print(i)
    return "That's all"

st = str(input())
print(perm(st))