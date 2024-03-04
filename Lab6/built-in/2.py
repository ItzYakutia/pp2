def caseCounter(s):
    upC = 0
    loC = 0
    for k in s:
        if ord(k[0]) > 64 and ord(k[0]) < 91:
            upC += 1
        if ord(k[0]) > 96 and ord(k[0]) < 123:
            loC += 1
    return upC, loC

st = "YEs i am not"
res = caseCounter(st)
print(f"Number of upper case letters: {res[0]}\nNumber or lower case letters: {res[1]}")