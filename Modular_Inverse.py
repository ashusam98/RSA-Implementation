import math
from Euler_phi_function import Phi_Function
from Modular_Exponentiation import Modular_Exponentiation

#This function computes the GCD of a and b where a>=b
def GCD(a,b):
    if(a%b==0):
        return b
    else:
        return GCD(b, a%b)

#This function computes the modular inverse of a w.r.t n
def Modular_Inverse(a,n):
    if(GCD(n,a)!=1):
        return -1
    else:
        l=Phi_Function(n)
        l=l-1
        k=Modular_Exponentiation(a,l,n)
        return k

if __name__ == "__main__":
    a=int(input("Enter a number to find its modular inverse: "))
    n=int(input("Enter the modulus: "))
    b=Modular_Inverse(a, n)
    print("The modular inverse of",a,"with modulus",n,"is",b)
