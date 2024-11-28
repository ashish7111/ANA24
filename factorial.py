# Factorial
# getting an input

num = input("Please enter a number that you want the factorial of: ")

num = int(num)


# Defining a new function that calls itself
def factor(n):
    if n == 1 or n == 0:
        return 1
    else:
        return factor(n-1) * n


# Printing the factorial of the given number
print(factor(num))

