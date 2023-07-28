#11
"""num=str(input("Enter a number: "))
i=len(num)
sum=0
x=0
while x <i:
    sum = sum + int(num[x])
    x = x+1
print (sum)

#12
num=str(input("Enter a number: "))
i=len(num)
product=1
x=0
while x <i:
    product = product * int(num[x])
    x = x+1
print (product)

#13
num=str(input("Enter a number: "))
i=len(num)
newnum=''
x=-1
while x >= -i:
    newnum += num[x]
    x = x-1
print (newnum)

#14
numwords = {0:"zero",1:"One",2:"Two",3:"Three",4:"Four",5:"five",6:"Six",7:"Seven",8:"Eight",9:"Nine"}
num=str(input("Enter a number: "))
i=len(num)
newnum=''
x=0
while x < i:
    a = int(num[x])
    check = numwords[a]
    newnum += numwords[a]
    x = x+1
print (newnum)

#15
num=input("Enter a number: ")
i=int(num)
first_num=1
second_num=1
x=3
if i <= 0:
    print("Please enter valid number")
elif i == 1:
    print(first_num)
elif i == 2:
    print(first_num, end=" ")
    print(second_num)
else:
    print(first_num, second_num, end=" ")
    while x <= i:
        sum = first_num + second_num
        print(sum, end=" ")
        first_num = second_num
        second_num = sum
        x = x + 1
#16
num=int(input("Enter a number: "))
product=1
x=1
while x <= num:
    product = product * x
    x = x+1
print (product)

#17
num=str(input("Enter a number: "))
i=len(num)
x=0
product = 0
while x < i:
  product = product + int(num[x])**3
  x = x+1
if product == int(num):
  print("Its a Armstrong number")
else:
  print("Its not a Armstrong number")

#18
num=int(input("Enter a number: "))
i=1
sum = 0
while i <= num:
  product = 1
  x = 1
  while x <= i:
    product = product * x
    x = x + 1
  sum += 1/product
  i = i + 1
print (sum)"""

#19
num_array = []
number = int(input("Enter a number: "))
num_array.append(number)
check_user = str(input("Do you want to enter another number?"))
if check_user != 'Yes' and check_user != 'yes' and check_user != 'No' and check_user != 'no':
  check_user = str(input("Please enter a valid response"))
while check_user != 'No' or check_user != 'no':
  if check_user == 'Yes' or check_user == 'yes':
    num_array.append(int(input("Please enter another number:")))
if check_user == 'Yes' or check_user == 'yes':
  num_array.append(int(input("Please enter another number:")))
elif check_user == 'No' or check_user == 'no':
  sum = 0
  i = 0
  length = len(num_array)
  while i < length:
    sum = sum + int(num_array[i])
  print(sum)