def isPal(st):
    if st[::-1] == st:
        return True
    return False

a = "madam"
print(isPal(a))