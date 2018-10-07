import math

#This code computes modular exponentiation in O(log n) time.
def Modular_Exponentiation(a, b, n):
    l=pow(a,b,n)
    return l

if __name__ == "__main__":
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    c = int(input("Enter the modulus: "))
    l = Modular_Exponentiation(a,b,c)
    print("The modular exponentiation of",a,"and",b,"with modulus",c,"is",l)