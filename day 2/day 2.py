#Q1 
''' 
age1 = int(input("enter age 1"))
age2= int(input("enter age 2"))
age3 = int(input("enter age 3"))
oldest= max(age1, age2, age3)
print (oldest)

'''

#Q3
'''
a= int(input("enter no 1 "))
b= int(input("enter no 2 "))
a,b= b,a
print(a,b)

'''

# #Q5
'''
num1= int(input("enter the number"))
num2= str(num1)
print(num2[::-1])

'''

#Q- Print product of two numbers by taking input from the user multiple times
'''
def product():
    num1= int(input("enter value of num1"))
    num2= int(input("enter value on num2"))
    print(num1*num2)

product()
product()
product()

'''

'''
no= int(input("how many times do u want the prodcut="))
for x in range(no):
    a= int(input("enter num 1"))
    b= int(input("enter num 2"))
    print(a*b)

'''
#Q7
'''
year= int(input("enter the year to be checked "))
if year%4 == 0  and year%400 ==0 :
    print("it is a leap year")
else:
    print("it is not a leap year")
'''

#Q8 
'''
x1= int(input("enter first x coordinate "))
x2= int(input("enter second x coordinate "))
y1= int(input("enter first y coordinate "))
y2= int(input("enter second y coordinate "))
print (((x2-x1)**2) + ((y2-y1)**2))

'''
#Q10
'''
cp= float(input("enter cost price "))
sp= float(input("enter selling price "))
if cp>sp:
    print("cost is more ")
else:
    print("selling price is more ")

'''
#Q12
'''
import math
radius= float(input("radius is "))
height= float(input("height is "))
vol= (math.pi)*(radius**2)*height
print (vol)

'''
#Q17
'''
num= int(input("enter no "))
sum = 0
while num!=0:
    rem = num%10
    sqr = rem*rem
    sum = sum+sqr
    num = int(num/10)

print(sum)
'''






