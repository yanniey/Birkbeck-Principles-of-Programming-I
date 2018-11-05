import math
try:
    n = float(input("Enter a number: "))
    m = math.sqrt(n)
    print("Square root of this number is", m)
except Exception as e:
    print("Your number is not correct. Here are more details: ", e)


