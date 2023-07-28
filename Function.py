#1
"""def num(a,b,c):
     print(max(a,b,c))
num(a=10, b=20, c=30)

#2
def sum (numbers):
    total=0
    for i in numbers:
        total= total+i
    return total
print(sum((8,2,3,0,7)))

#3
def mul(numbers):
    total=1
    for i in numbers:
        total= total*i
    return total
print(mul((8,2,3,-1,7)))

#4
def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str

s = "1234abcd"

print("The original string is : ",s, end="\n")
print("The reversed string is : ",reverse(s), end="")

#5
def fact(num):
    if num==0:
        return 1
    else:
        return num * fact(num-1)

num= int(input("Enter a number"))
print(fact(num))

#6
def test_range(num):
    fn= int(input("Enter the first number:"))
    sn= int(input("Enter the second number:"))
    if num in range(fn, sn+1):
        print("%s is in the range"%str(num))
    else:
        print("%s is out of range")
num= int(input("Enter a number"))
test_range(num)

#7
def string_test(s):
    d= {"UPPER CASE":0, "LOWER CASE":0}
    for c in s:
        if c.isupper():
            d["UPPERCASE"]+= 1
        elif c.islower():
            d["LOWERCASE"]+= 1
        else:
            pass

s= 'The quick Brow Fox'
print("Original string",s)
print("Number of upper string:", d["UPPERCASE"])
print("Number of lower string:", d["LOWERCASE"])

#8
def my_list(l):
    x=[]
    for i in l :
        if i not in x:
            x.append(i)
    return x
print(my_list([1,2,3,3,3,3,4,5]))

#9
def test_prime(n):
    if (n==1):
        return False
    elif (n==2):
        return True;
    else:
        for i in range (2,n):
            if (n%i==0):
                return False
        return True

print(test_prime(17)

#10
def test_even(l):
    x=[]
    for i in l:
        if i%2==0:
            x.append(i)
    return x
print(test_even([1, 2, 3, 4, 5, 6, 7, 8, 9]))"""

import numpy as np
a = np.array([1, 0, np.nan, np.inf])
print("Original array")
print(a)
print("Test a given array element-wise for finiteness :")
print(np.isfinite(a))

