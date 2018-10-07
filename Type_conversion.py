import math
import string

#This code converts string to binary digits from (8-bits ASCII)
def string_to_bits(str1):
    l = [bin(ord(ch))[2:].zfill(8) for ch in str1]
    return l

def bin_to_dec(bin1):
    k = [int(b,2) for b in bin1]
    return k

def dec_to_bin(num1):
    k = [bin(c)[2:].zfill(8) for c in num1]
    return k

def bin_to_string(bin1):
    k = [chr(int(b1,2)) for b1 in bin1]
    return k


if __name__ == "__main__":
    a = input("Enter a string: ")
    print(a)
    x = string_to_bits(a)
    print (x)
    y = bin_to_dec(x)
    print (y)
    y1 = dec_to_bin(y)
    print(y1)
    x1 = bin_to_string(y1)
    print (x1)