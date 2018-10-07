import math
from Modular_Exponentiation import Modular_Exponentiation
from Modular_Inverse import Modular_Inverse
from Modular_Inverse import GCD
from Type_conversion import string_to_bits
from Type_conversion import bin_to_string
from Type_conversion import bin_to_dec
from Type_conversion import dec_to_bin
from Euler_phi_function import is_prime
from Euler_phi_function import Phi_Function

#This code stores all the possible values of public key e in a list and asks user to choose
#the index of public key. Here, e=1, is excluded since corresponding to it's modular inverse d=1 is obvious.
def key_generation(n):
    i=2
    l=[]
    while(i<=n):
        if(GCD(n,i)==1):
            l.append(i)
        i=i+1
    return l

#This function outputs the RSA encrypted ciphertext.
def encryption(m, e, n):
    c=Modular_Exponentiation(m, e, n)
    return c

#This function outputs the RSA decrypted plaintext.
def decryption(c, d, n):
    m=Modular_Exponentiation(c, d, n)
    return m

if __name__ == "__main__":

    p1=int(input("Enter the first prime number: "))
    while(not is_prime(p1)):
        p1=int(input("The number is not prime. Enter again: "))

    q1=int(input("Enter the second prime number: "))
    while(not is_prime(q1)):
        q1=int(input("The number is not prime. Enter again: "))

    n=p1*q1
    print("The generated value of modulus is",n)
    phi=(p1-1)*(q1-1)
    r2=Phi_Function(phi)
    key=key_generation(phi)
    ind=int(input("Enter an index from 1 to "+str(r2-1)+" for generating a public key: "))
    while(ind<1 or ind>r2-1):
        ind=int(input("Index out of range. Enter again: "))
    e=key[ind+1]
    d=Modular_Inverse(e,phi) #private key
    print("The public key is",e)
    print("\n")

    pt=input("Enter the plaintext message: ")
    m=bin_to_dec(string_to_bits(pt))
    c=[encryption(u1,e,n) for u1 in m]
    ct=bin_to_string(dec_to_bin(c))
    print("The encrypted cipher text is","".join(ct))

    d1=[decryption(u2,d,n) for u2 in c]
    dt=bin_to_string(dec_to_bin(d1))
    print("The decrypted plain text is: ","".join(dt))
