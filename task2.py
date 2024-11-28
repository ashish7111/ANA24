# Simple calculator method

# Prompt user for 2 numbers and a third input for the operation
a, b, c = input("Enter two numbers and an operation you want to perform (Add/Subtract/Multiply/Divide").split()
a = int(a)
b = int(b)

if c == 'Add':
    print(a+b)
elif c == "Multiply":
    print(a*b)
elif c == 'Subtract':
    print(a-b)
elif c == 'Divide':
    print(a-b)
else:
    print("Something went wrong")

