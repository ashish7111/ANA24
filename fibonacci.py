# fibonacci series
# Getting input for number of terms from the user

terms = int(input("Enter the number of terms you want in this series"))

n1 = 0
n2 = 1
count = 0

# Checking for negative numbers
if terms < 0:
    print('Please enter positive numbers')

# Printing default values
elif terms == 0:
    print(0)
elif terms == 1:
    print(n1)
else:
    while count < terms:
        print(n1)
        temp = n1 + n2
        n1 = n2
        n2 = temp
        count += 1
