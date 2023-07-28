#1a
"""i=0
for i in range (1,11):
    print(i*2)

#b
for i in range (1,20):
    if i%2!=0:
        print(i)

#2
n=1
print("Numbers:", "\t\t", "Squares")
for n in range (1,11):
    print(n,"\t\t\t", n**2)

#3
for n in range(10,301,10):
    print(n,end= ' ')

#4
for n in range(105,0,-7):
    print(n, end=' ')

#5
for n in range(10,0,-1):
    print(n, end=' ')

#6
sum=0
for n in range(1,11):
    sum=sum+n
print(sum)

#7
sum=0
for i in range (1,21):
    if i%2==0:
        sum=sum+i
print(sum)

#8
n=int(input("Enter a number"))
for i in range(1,11):
    print(n,'*',i,'=',n*i)

#9
n1=int(input("Enter first number"))
n2=int(input("Enter second number"))
if n2>n1:
    for n1 in range (n1, n2+1):
        if n1%2==0:
            print(n1)
else:
    for n2 in range (n2, n1-1):
        if n2%2==0:
            print(n2)

#10
n=int(input("Enter a number"))
if n==0 or n==1:
    print("Number is not prime")
else:
    for i in range (2,n):
        if n% i!=0:
            print("Number is prime")

#11
n=int(input("Enter a number"))
sum=0
for digit in str(n):
    sum= sum + int(digit)
print(sum)

#12
n=int(input("Enter a number"))
prod=1
for digit in str(n):
    prod= prod* int(digit)
print("Product:", prod)

#13
n= int(input("Enter a number"))
rev=0
for i in range (len(n),0,-1):
    a= str
    rev= rev+ int(n[i-1])
print("Reverse:", rev)

#14
nw = {0:"zero",1:"One",2:"Two",3:"Three",4:"Four",5:"five",6:"Six",7:"Seven",8:"Eight",9:"Nine}
n= str(input("Enter a number"))
for nw in range (0,)

#15
n=int(input("Enter no. of terms"))
n1=0
n2=1
sum=1
count=1
for count in range (1,n+1):
    n1=n2
    n2=sum
    sum=n1+n2
    print(n1, end=' ')

#16
n=int(input("Enter a number"))
i=1
factorial=1
for i in range (1,n+1):
    factorial= factorial*i
print(factorial)

#17
n=str(input("Enter a number"))
i=len(n)
x=0
product=0
for x in range (1,i):
    product= product+ int(n[x])**3
if product== int(n):
    print("Number is Armstrong")
else:
    print("Number is not Armstrong")

#18
n=int(input("Enter a number"))
sum=1
fact= 1
for i in range (1,n+1):
    fact= fact*i
    sum= sum+(1/fact)
print(sum)

#19
n=int(input("Enter a number"))
sum=0
for i in range(1,)
n1= int(input("Enter another number"))
sum= sum+n+n1
n1= str(input("Do you want to continue"))
print(sum)

#20
count_pos=0
count_neg=0
n=1
for i in range (0,n):
    n=int(input("Enter a number"))
if n>0:
    count_pos = count_pos+1
elif n<0:
    count_neg= count_neg+1
elif n==0:
    break
print("Number of positive and negative numbers:", count_pos,count_neg)

#22
n=int(input("Enter a number"))
rem=0
bin=1
p=1
for n in range
    rem= n%2
    bin=bin+ (rem*p)
    p= p*10
    n=n//2
print("Binary:",bin)

#24
n= str(input("Enter a number"))
n_r= str(n[::-1])
if n==n_r:
    print("Palindrome")
else:
    print("Not palindrome")

#26
n1 = int(input("Enter a number"))
sum=0
avg=0
for count in range(1,10):
    n2= int(input("Enter another number"))
    sum= sum+ n1+n2
    avg= sum/(count+1)
print("Average:", avg)

#27
n1 = int(input("Enter a number"))
for count in range(1,10):
    n2= int(input("Enter another number"))
print(max(n1,n2), min(n1,n2))

#28
n1 = int(input("Enter a number"))
n2= int(input("Enter another number"))
sum_odd=0
sum_even=0
if n1>n2:
    for i in range (n2, n1+1):
        if n2%2==0:
            sum_even= sum_even+n1
        else:
            sum_odd= sum_odd+n2

else:
    for i in range (n1, n2+1):
        if n1%2==0:
            sum_even= sum_even+ n1
        else:
            sum_odd = sum_odd+n1
print("Sum of even nos:",sum_even, "and Sum of odd nos:",sum_odd)

#29
n1=100
n2=500
for i in range(100,501):
    if i% 13==0 and i%3!=0:
        print(i)

#30
n= int(input("Enter no of terms"))
st= '2'
for i in range (1,n+1):
    print(st, end=' ')
    st= st+'2'

#31
n= int(input("Enter no of terms"))
x=1
for i in range(1,n+1):
    x = i**2
    print(x, end= ' ')

#32
n= int(input("Enter no of terms"))
x= int(input("Enter a number"))
fact=1
sum=1
for i in range(1, n):
    fact = fact * i
    sum= sum+ ((x**i)/fact)
print(sum)

#33
n= int(input("Enter no of terms"))
x= int(input("Enter a number"))
sum=1
for i in range(1, n+1):
    sum= sum+ ((x**i)/i)
print(sum)

#34
n= int(input("Enter no of terms"))
sum=0
for i in range (1,n+1):
    sum= sum +(i**3)
print(sum)

#35
n= int(input("Enter no of terms"))
sum=0
prod=1
for i in range(1,n+1):
    prod = prod * i
    sum = sum + prod
print(sum)

#36
n= int(input("Enter no of terms"))
sum=1
for i in range(2,n+1):
    if i%2==0:
        sum= sum+i**2
    else:
        sum= sum-i**2
print(sum)

#37
str= "PYTHON"
for i in range (0,len(str)):
    print(str[i])

#38
L= [23,45,32,25,46,33,71,90]
for num in L:
    if num%2==1:
        print(num)

#39
n= int(input("Enter a number"))
for i in range(1,n+1):
    if n%i==0:
        print(i)

#40
x=49
for i in range(1,50):
    print(i,"----",x)
    x=x-1"""











