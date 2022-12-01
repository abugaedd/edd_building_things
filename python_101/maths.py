# Asks user to input 2 values and store them in variables num1 and num2
# split is a command that enables one take more inputs divided by space

num1, num2 = input('Enter 2 numbers: ').split()

# convert the strings into regular numbers integer

num1 = int(num1)
num2 = int(num2)

# Add the values entered and store them in sum

sum = num1 + num2

# Substract vaalues and store them in difference

difference = num1 - num2

# Multiply the values and store in product

product = num1 * num2

# Divide the values and store them in quotient

quotient = num1 / num2

# Use modulus on the values to find the remainder

remainder = num1 % num2

# print the results
print("{} + {} = {}".format(num1, num2, sum))
print("{} - {} = {}".format(num1, num2, difference))
print("{} * {} = {}".format(num1, num2, product))
print("{} / {} = {}".format(num1, num2, quotient))
print("{} % {} = {}".format(num1, num2, remainder))
