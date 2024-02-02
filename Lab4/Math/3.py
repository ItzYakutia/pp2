import math

num = int(input("Input number of sides: "))
leng = int(input("Input the length of a side: "))

a = int(1/4 * num * (leng ** 2) * (1/math.tan(math.pi/num)))
print("The area of the polygon is:", a)
