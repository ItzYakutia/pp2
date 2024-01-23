"""
a = int(input())
b = 200
if b > a:
  print("b is greater than a")
elif b == a:
    print("a = b")
else:
    print("a is greater than b")
    
if a > b: print("a is greater than b")


print("a is greater than b") if a > b else print("b is greater than a")
"""

a = 13
b = 200
c = 15
if a < b and c < b:
    print("Both cond are True")
    
if a < b or c < b:
    print("One or two cond are True")
    
if not(a > b):
    print("a not greater than b")
    
x = 15
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    pass
    

