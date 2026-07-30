'''
#input formatting-->accepting input from user--->input()
#accepting integer input from user
#by deafult input() accept any input-->str
#int(input())--.will accept only integer
age = float(input('enter the age:'))
print(type(age))
#float(input())-->accepts int float values
#accepting string input from user
name=input("enter the name:")
print(type(name))
#accepting group values
marks=int(input("enter the marks")).split()
print(marks)

a=input().split()
print(a)
a = input("enter the values:").split(',')
print(a)
#list of integer
marks=list(map(int,input("enter the values").split(',')))
print(marks)

#now we want to accept 2 values from user
age,salary = map(int,input("enter the values").split(','))
print(age)
print(salary)

#single input---> int(input())
#two inputs-->a,b=main(int,input().split(','))
#any number result as list-->a=list(map(int,input().split(',')))

age,salary = map(float,input("enter the values").split(','))
print(age)
print(salary)

marks=list(map(float,input("enter the values").split(',')))
print(marks)

#accepting input from user-->int,float-->input formatting
#operators-->operators perform operation between values(operaters)
# 7types -->arthimetic,assignment,comparision(relationship)
#membership,identity,logical,bitwise
#arthematic operators
print(5+3)
print(5-3)
print(5*3)
print(5/3)#float type
print(5//3)#quotient
print(5%3)#reminder(modules)
print(5**3)#power(exponential)

#task-->accept integer input as length,breath-->find the area of rectangle
#area = lengt*breath
length=int(input("enter the values"))
breath=int(int(input("enter the values")))
area=length*breath
print(area)
length*breath= map(int(input("enter the values").split(',')))
print(length*breath)
'''
#assigment operators-->asign values
#=,+=,-=
a=45
print(a)
#update the value of a
a = a + 5#a+= 5
print(a)
b=35
b += a #b = b+ a
print(b)
b -= 5
print(b)
#task *=,/=,//=,%=,**=
c=5
c *= 2
print(c)
c *= a
print(c)
b /= c
print(b)
b //= c
print(b)
b %= c
print(b)
d=2
d **= 2
print(d)

'''
#comparision operators-->we compare the values-->boolen
# ==(equal to),!=(not equal to),<(less than),>(greater than)
# <=(less than or equal to),>=(greater than or equal to)
age=25
print(age==25)
print(age!=35)
print(age<=25)
print(age>=25)
print(age>35)
print(-5<-1)

#membership operator-->in,,not in-->boolen
#it checks for the existing of an object in a collection
marks = [23,34,45]
print(22 in marks)
print(33 not in marks)
print('code' in 'codegnan')#str
#logical operators--->logical decision making---> and,or,not
#and-->all condition to b satisfied
#or==>any one condition
a = (25 in[25,34,45] and 56>45)
print(a)
b = 45>56 or 25<=45
print(b)
c = not(True)
print(c)
#identity operators-->check for indentity of an object-->id()
a=35
b=35
print(id(a))
print(id(b))
print(a is b)
c=a
print((id(c))
print(c is a)

a=[1,2,3,4]
print(id(a))
c = a
print(c is a)
'''
      



















































































