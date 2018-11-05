def my_factorial(n):
    if n<1:
        raise ValueError("Factorial defined for positive numbers only")
    product =1
    for i in range(1,n+1):
        product*=i
    return product

try:
    print(my_factorial(-2))
except:
    print("Problem")
