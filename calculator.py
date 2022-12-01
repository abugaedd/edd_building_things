# calculator
# store the user input of 2 numbers and the operator

num1, operator, num2 = input('Enter Calculation: ').split()

# Convert the strings into integers

num1 = int(num1)
num2 = int(num2)

# calculation is done according to operator

if operator == "+":
    print("{} + {} = {}".format(num1, num2, num1 + num2)
elif operator == "-":
          print("{} - {} = {}".format(num1, num2, num1 - num2))
elif operator == "/":
          print("{} / {} = {}".format(num1, num2, num1 / num2))
elif operator == "*":
          print("{} * {} = {}".format(num1, num2, num1 * num2))
elif operator == "%":
          print("{} % {} = {}".format(num1, num2, num1 % num2))
else:
          print("use either + - / % * ")
