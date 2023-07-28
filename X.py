n1= str(input("Enter a number"))
j= len(n1)
n2= []
for i in range(j-1,-1,-1):
    n2.append(n1[i])
n= ("".join(n2))
if n1== n:
    print("It is palindrome")
else:
    print("Its not")