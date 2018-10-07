import math

#This code returns the modular sum of two integers.
def mod_addition(a, b, n):
    mod = a%n + b%n
    mod = mod%n
    return mod

if __name__ == "__main__":
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    n = int(input("Enter the modulus: "))
    l = mod_addition(a,b,n)
    print("The modular sum of",a,"and",b,"is",l,"with modulus",n)