import math
print("Welcome to the 3d shape calculator")
print("chose a option from the options menu")
print("1.Cube")
print("2.Sphere")
print("3.rectangular prism")
print("more soon")
choice = input("enter your choice: ")
if choice == "1":
    edge = float(input("enter the size of the edge without unit: "))
    volume = edge * edge * 6
    print(f"The volume of the prism is: {volume}")
elif choice == "2":
    radius = float(input("enter the radius of the prism without unit: "))
    volume = radius * radius * 4 * math.pi
    print(f"The volume of the prism is: {volume}")
elif choice == "3":
    length = float(input("enter the length of the prism without unit: "))
    width = float(input("enter the width of the prism without unit: "))
    high = float(input("enter the high value of the prism without unit: "))
    volume = length * width * high
    print(f"The volume of the prism is: {volume}")


