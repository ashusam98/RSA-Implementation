import math

#This code returns the modular product of two integers.
def mod_multiplication(a, b, n):
    mod = a%n * b%n
    mod = mod % n
    return mod

if __name__ == "__main__":
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    c = int(input("Enter the modulus: "))
    l = mod_multiplication(a, b, c)
    print("The modular product of",a,"and",b,"is",l,"with modulus",c)