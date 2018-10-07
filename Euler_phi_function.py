import math

#This function finds the greatest integer less than or equal to square root of input
def integer_root(n):
    i=0
    while(pow(i,2)<=n):
        i=i+1
    return i

#This function checks whether a number is prime or composite.
def is_prime(p):
    i=2
    l=integer_root(p)
    if(p==1):
        return False

    while(i<l):
        if(p%i==0):
            return False
        else:
            i=i+1
    return True

#This function computes the highest power of p that divides n
def prime_power(n, p):
    i=0
    a=n
    while(a%p==0):
        a=a/p
        i=i+1
    return i

#This function computes the phi function
def Phi_Function(n):
    i=2
    m=1
    while(i<=n):
        if(is_prime(i) and n%i==0):
            k=prime_power(n,i)
            m=m*pow(i,k-1)*(i-1)
        i=i+1
    return m

if __name__ == "__main__":
    a=int(input("Enter a number to find its phi function: "))
    m=Phi_Function(a)
    print("The phi function of",a,"is",m)