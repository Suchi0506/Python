#1
"""for i in range(1,11):
    if i % 2 == 0:
        continue
    print(i*i)

#2
month_list=['January', 'February','March','April','May']
expense_list = [2340, 2500, 2100, 3100, 2980]
e=input("Enter expense amount:")
e=int(e)

#3
month=-1
for i in range(len(expense_list)):
    if e==expense_list[i]:
        month=i
        print(month_list[month])
    else:
        if (month == -1):
            print("expense amount not found")
            break

#4
age=input("Enter age")
age=int(age)
if(age>=18):
    print("Eligible for voting")
else:
    print("Not elgible for voting")

#5
=int(input("Enter a number"))
if n%2 == 0:
    print("Number is even")
else:
    print("NUmber is odd")

#6
n=int(input("Enter a number"))
if n%7==0:
    print("Number is divisible by 7")
else:
    print("Number is not divisible by 7")

#7
n=int(input("Enter a number"))
if n%5==0:
    print("Hello")
else:
    print("Bye")

#8
u=int(input("Enter number of unit"))
if u<=100:
    print("No charge")
elif u<=200 and u>100:
    print("Price is:",(u-100)*5)
elif u>200:
    print("Price is:",500+(u-200)*10)

#9
u=int(input("Enter number of unit"))
print("last digit of number is:",n%10)

#10
u=int(input("Enter number of unit"))
last_digit=u%10
if last_digit%3==0:
    print("Number is divisible by 3")
else:
    print("Number is not divisible by 3")

#11
u=int(input("Enter marks"))
if u>90:
    print("Grade A")
elif u>80 and u<=90:
    print("Grade B")
elif u>=60 and u<=80:
    print("Grade C")
elif u<60:
    print("Grade D")

#12
cp=int(input("Enter the cost price of the bike"))
tax=0
if cp>1000000:
    tax= (15/100) * cp
elif cp>50000 and cp<=100000:
    tax= (10/100) * cp
elif cp<=50000:
    tax= (5/100) * cp
print("the road tax to be paid:", tax)

#13
year=int(input("Enter the year"))
if year%4== 0:
    print("this is a leap year")
else:
    print("this is not a leap year")

#14
num=[1,2,3,4,5,6,7]
days=['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Friday', 'Saturday']
num=int(input("Enter any number between 1-7:"))
if num==1:
    print("Sunday")
elif num==2:
    print("Monday")
elif num==3:
    print("Tuesday")
elif num==4:
    print("Wednesday")
elif num==5:
    print("Thursday")
elif num==6:
    print("Friday")
elif num==7:
    print("Saturday")
else:
    print("Enter valid input")

#15
num=[1,2,3,4,5,6,7,8,9,10,11,12]
m_d=[['January,31'], ['February,28'], ['March,31'], ['April,30'], ['May,31'], ['June,30'], ['July,31'], ['August,31'], ['September,30'], ['Ocotber,31'], ['November,30'], ['December,31']]
num=int(input("Enter number between 1-12:"))
if num==1:
    print("January,31")
elif num==2:
    print("February,28")
elif num==3:
    print("March,31")
elif num==4:
    print("April,30")
elif num==5:
    print("May,31")
elif num==6:
    print("june,30")
elif num==7:
    print("July,31")
elif num==8:
    print("August,31")
elif num==9:
    print("September,30")
elif num==10:
    print("October,31")
elif num==11:
    print("November,30")
elif num==12:
    print("December,31")
else:
    print("Enter valid number")

#16
A=int()
B=int()
C=int()
D=int()
if A>B:
    print("A is greater than B")
elif C>D:
    print("C is greater than D")

#17
ci= ["Delhi", "Agra", "Jaipur"]
city= input("Enter city name")
if city== "Delhi":
    print("Monument:Red fort")
elif city== "Agra":
    print("Monument:Taj Mahal")
elif city== "jaipur":
    print("Monument:Jal Mahal")
else:
    print("Enter valid city")

#18
num=int(input("Enter a number"))
if num>99 and num<1000:
    print("Number is three digit number")
else:
    print("Number is not three digit number")

#19
num1 =int(input("Enter a number"))
num2 =int(input("Enter a number"))
if num1> num2:
    print("The smaller number is:",num2)
else:
    print("The smaller number is:",num1)

#20
num =int(input("Enter a number"))
if num>0:
    print('Number is positive')
else:
    print("Number is negative")

#21
num =int(input("Enter a number"))
if num%2==0 and num%3==0:
    print("Number is divisible by 2 and 3")
else:
    print("Number is not divisible by 2 and 3")

#22
num1 =int(input("Enter a number"))
num2 =int(input("Enter a number"))
num3 =int(input("Enter a number"))
if num1> num2 and num1>num3:
    print("the largest number is :",num1)
elif num2>num1 and num2>num3:
    print("the largest number is :",num2)
elif num3>num1 and num3>num2:
    print("the largest number is: ",num3)

#23
temp=float(input("Enter a temperature value"))
if temp>=100:
    print("Water is boiling")
else:
    print("water is not boiling")"""

#24
"""Every prime number can be written in the form of 6n + 1 or 6n – 1 (except the multiples of prime numbers, 
i.e. 2, 3, 5, 7, 11), where n is a natural number.
n= int(input("Enter a number"))
i=[2,3,5,7,11]

if n= (6n+1)% {i}!==0 or n= (6n-1)% {i}!==0:
    print("Number is prime")
else:
    print("Number is not prime")
    i+=1"""


#25
"""n=int(input("Enter total number of working days"))
m=int(input("Enter total number of days absent"))
percentage= (n-m)/n *100
if percentage>75:
    print("Student eligible for exam")
else:
    print("Student not eligible for exam")

#26
age=int(input("Enter the age"))
sex= str(input("Enter sex"))
days= int(input("Enter days"))

if age>=18 and age<30 and sex== 'M':
    total= 700*days
    print("Total wages is:",total)
elif age >= 18 and age < 30 and sex == 'F':
     total = 750 * days
     print("Total wages is:", total)
elif age >= 30 and age < 40 and sex == 'M':
     total = 800 * days
     print("Total wages is:", total)
elif age >= 30 and age < 40 and sex == 'F':
     otal = 850 * days
     print("Total wages is:", total)
else:
    print("Enter appropriate age")

#27
u= int(input("Enter the electric unit"))

if u<=100:
    amount=0
    print("No charge")
elif u<=200 and u>100:
    amount= (u-100)*2
    print("Total bill:",amount)
elif u>=300:
    amount= 400+(u-300)*5
    print("Total bill:", amount)

#28
d= int(input("Enter the number of days"))
if d<=5:
    amount= d*2
elif d>=6 and d<=10:
    amount= d*3
elif d>=11 and d<=15:
    amount= d*4
elif d>15:
    amount= d*5
print("The charge for library:", amount)"""






















