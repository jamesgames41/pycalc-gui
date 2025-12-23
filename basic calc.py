n1 = int(input("first number: "))
n2 = int(input("second number: ")) # Removed the extra spaces at the start
n3 = None
op = input("operation: ")

if op == "+": n3 = n1 + n2
elif op == "-": n3 = n1 - n2
elif op == "*": n3 = n1 * n2
elif op == "/": n3 = n1 / n2
print(n3)
