import math
from turtledemo.round_dance import stop
l = None
w = None
r = None
b = None
h = None

print("Welcome to the 2d area calculator")
print ("chose a shape from the following options:")
print("1) Rectangle/square")
print("2) Circle")
print("3) Triangle")
print("more soon")
choice = input("Enter your choice: ")
if choice == '1':
 l = float(input("length without unit"))
 w = float(input("width without unit"))
 area = l * w
 print (f"The area of the rectangle is {area}cm")
elif choice == '2':
 unit = input("What unit is your radius?")
 r =  float(input("Radius without unit"))
 area = r * r * math.pi
 print (f"The area of the circle is {area}{unit}")
elif choice == '3':
 b = float(input("base without unit"))
 h = float(input("hight without unit"))
 area = h * b /2
 print (f"The area of the triangle is {area}")




