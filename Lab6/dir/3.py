import os

def check(p):
    if os.path.exists(p):
        print("Exist")
        print(os.path.basename(p))
        print(os.path.dirname(p))
        return True
    else:
        print("Doesn't exist")
        return False

pa = os.getcwd()

print(check("/Users/yxk/yesyep"))
