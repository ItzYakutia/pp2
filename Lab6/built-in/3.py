def isPal(s):
    if s == s[::-1]:
        return True
    return False

st = "ababa"

print(isPal(st))