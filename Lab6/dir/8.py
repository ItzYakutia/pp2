import os

p1 = "/Users/yxk/yesyep/lab6/dir/5.txt"

if os.path.exists(p1):
    if os.access(p1, os.W_OK):
        os.remove(p1)