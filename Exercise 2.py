#1 first 10 even numbers
"""n=2
while n<=20:
    print(n)
    n=n+2

#2 first 10 integers and their squares
n=1
print("Numbers\t\tSquares")
while n<=10:
    print(n,"\t\t\t",n**2)
    n=n+1

#3 print10-300
n=10
while n<=300:
    print(n)
    n=n+1

#4 loop statement to print 105....7
n=105
while n>=7:
    print(n)
    n=n-7

#5
n=10
while n>=1:
    print(n)
    n=n-1

#6
n=0
sum=0
while n<=10:
    sum= n+sum
    n=n+1
    print(sum)

#7
n=2
sum=0
while n<=10:
    n=n+2
    sum=sum+n
    print(sum)

#8 table of any number
n=int(input("Enter a number"))
i=1
while i<=10:
    print(n,"*",i,"=", n*i)
    i=i+1

#9
n1=int(input("Enter first number"))
n2=int(input("Enter second number"))
if n1>n2:
    while(n1>n2):
        if n2 % 2==0:
            print(n2)
        n2=n2+1
else:
    while (n2>n1):
        if n1 % 2==0:
            print(n1)
        n1= n1+1

#11
n=int(input("Enter a number"))
sum=0
while(n>0):
    remainder=n%10
    sum= sum+remainder
    n= n//10
print('Sum of digits of a number:',sum)

#12
n=int(input("Enter a number"))
while(n>0):
    r=n%10
    n= n//10
    product=r*n
    break
print('Product of digits of a number:',product)

#13
n=int(input("Enter a number"))
while(n>0):
  remainder = n % 10
  n = n // 10
  reverse= remainder*10+ n*1
  break
print('Reversed number:',reverse)

#14
num= str(input("Enter a number"))
numwords= {0:"zero",1:"One",2:"Two",3:"Three",4:"Four",5:"five",6:"Six",7:"Seven",8:"Eight",9:"Nine"}
i=len(num)
new=" "
x=0
while x<i:
    a=int(num[x])
    check= (numwords[a])
    x=x+1
    new+= numwords[a]
print(new)

#15
n=int(input("Number of terms you want Fibonacci series in:"))
num1=0
num2=1
sum=1
count=1
while (count<= n):
    num1= num2
    num2= sum
    sum= num1+ num2
    count += 1
    print(num1,end=' ')

#16
n=int(input("Enter a number"))
factorial=1
i=1
while(i<=n):
    factorial= factorial*i
    i+=1
print("Factorial of number:", factorial)

#17
n= str(input("Enter a number"))
i= len(n)
x=0
product=0
while(x<i):
    product= product+ int(n[x])**3
    x=x+1
if product== int(n):
    print("Number is Armstrong")
else:
    print("Number is not Amstrong")

#18
n= int(input("Enter a number"))
f=1
i=1
sum=0
while(i<=n):
    f=f*i
    i=i+1
    sum= sum+(1/f)
print("Sum:",sum)

#19
n= int(input("Enter a number"))
sum=0
i= 'y'
while (i=='y'):
    n1= int(input("Enter another number"))
    sum = sum +n+ n1
    i = str(input("Do You Want To Continue?"))
print("Sum of numbers:", sum)

#20
n=1
count_pos=0
count_neg=0
while(n!=0):
    n= int(input("Enter a number"))
    if n>0:
        count_pos= count_pos+1
    elif n<0:
        count_neg= count_neg+1
    elif n==0:
        break
print("Number of positive and negative numbers resp:",count_pos, count_neg)

#21
x= int(input("Enter first number"))
y= int(input("Enter second number"))
hcf=1
if x>y:
    for i in range(1,y+1):
        if (x% i==0) and (y% i==0):
            hcf=i
print("hcf is:", hcf)

#22
n= int(input("Enter a number"))
rem=0
bin=0
p=1
while n>0:
    rem= n%2
    bin=bin+ (rem*p)
    p= p*10
    n=n//2
print("Binary:",bin)

#23
n=int(input("Enter a binary number"))
decimal=0
power=1
rem=0
while(n>0):
    rem= n%10
    n= n//10
    decimal= decimal +(rem*power)
    power= power*2
print("Number is:", decimal)

#24
n=int(input("Enter a number"))
onum=n
rem=0
i=0
len=len(str(onum))
rnum=0
while i<len:
    rem= n %10
    rnum = rnum * 10 + rem
    n= n//10
    i=i+1
if onum==rnum:
    print("Number is palindrome")
else:
    print("Number is not palindrome")

#25
n=int(input("How many terms"))
s=1
f=1
i=1
while(i<=n):
    f= i*f
    s=s+(1/f)
    i = i + 1
print(s)

#26
n= int(input("Enter a number"))
sum=0
count=1
while(count<10):
    i=int(input("Enter a number"))
    sum=sum+ i+ n
    average= sum/(count+2)
    count= count+1
print("Average of numbers:", average)

#27
list= []
num= int(input("How many numbers:"))
for n in range(num):
    i=int(input("Enter a number"))
    list.append(i)
    largest= max(list)
    smallest= min(list)
print("The largest number is:",largest, "\nThe smallest number is:", smallest)

#28
n1= int(input("Enter first number"))
n2= int(input("Enter second number"))
sum_even=0
sum_odd=0
if n2>n1:
    while n1<=n2:
        if n1%2==0:
            sum_even= sum_even+ n1
            n1= n1+1
        else:
            sum_odd=sum_odd+n1
            n1=n1+1
else:
    while n2<=n1:
        if n2%2==0:
            sum_even= sum_even+n2
            n2=n2+1
        else:
            sum_odd= sum_odd+n2
            n2=n2+1
print("Sum of even numbers:",sum_even)
print("Sum of odd numbers:",sum_odd)

#29
n=101
while(n<500):
    if n%13==0 and n%3!=0:
        print(n)
    n=n+1

#30
n=int(input("How many terms:"))
st='2'
i=0
while i<n:
    print(st,end=',')
    st= st+'2'
    i=i+1

#31
n=int(input("How many terms:"))
i=1
while i<=n:
    print(i**2, end=' ')
    i=i+1

#32
x=int(input("Enter a number"))
n= int(input("Enter how many terms"))
s=1
f=1
i=1
for i in range (1,n+1):
    f=f*i
while(i<=n):
    s=s+((x**i)/f)
    i = i + 1
print(s)

#33
x=int(input("Enter a number"))
n= int(input("Enter how many terms"))
s=0
i=1
while(i<=n):
    s=s+(x**i)/i
    i=i+1
print(s)

#34
n= int(input("Enter how many terms"))
s=0
i=1
while(i<=n):
    s=s+(i**3)
    i=i+1
print(s)

#35
n= int(input("Enter how many terms"))
i=1
s=0
prod=1
while(i<=n):
    prod= prod*i
    s= s+prod
    i=i+1
print(s)

#36
n= int(input("Enter how many terms"))
i=2
s=1
while(i<=n):
    if i%2==0:
        s=s+i**2
        i=i+1
    else:
        s= s-i**2
        i=i+1
print(s)

#37
str= "PYTHON"
i=0
while i< len(str):
    print(str[i])
    i=i+1

#38
L= [23,45,32,25,46,33,71,90]
i=0
while (i<len(L)):
    if L[i]%2 !=0:
        print(L[i])
    i=i+1

#39
n=int(input("Enter any number"))
i=1
while i<=n:
    if n%i==0:
        print (i)
    i=i+1

#40
i=1
x=49
while i<=49:
    print(i,"-----",x)
    i=i+1
    x=x-1"""











































