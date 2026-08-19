'''
procedure oriented programming
functions-->a function is a block of code which perform a specific task
its a reusable group of statements where we define using
def keyword
advantsges-->code resuability,code mentainabilitty,ease of debuggin,
avoiding code duplication,modularity
def fname(parameters):  function defn
     """Doc string"""(description)
     statements(s)....    function body
     .....
     return value(s)...
fname(arguments)          function call
'''
#to perfrom sum of given objectes
'''
def add(a,b):
    """sum of objects"""
    c=a+b
    return c
print(add(12,3))#addition
print(add('code','gnan'))#concatenation
print(add([12,5],[12,34]))#merging
c,d=map(int,input("enter the values:").split(','))
print(c,d)
print(add(c,d))

def add(a,b):
    """sum of objects without return"""
    print(a+b)
add('code','gnan')
print(add(12,-35))#it retrun results along with none

name,age,salary="anjum",21,50000
#usage of return
def details():
    #return name,age,salary
    #return "codegnan"
    #return 23+34+45
    return  #it return none in output

print(details())

they are 5 types of arguments
--->positional arguments
--->default arguments
-->keyword arguments
-->vairable length arguments(*args)
-->keyword vairable length arguments(**kwargs)

#positional arguments -->number of arguments in function defn should
#match with function call (order has to be maintained)
#print(len(123,234)) this is as per built in len(obj) will accept one args
def details(name,place):
    """to store the details"""
    #name="codegnan"
    #place="kukatpally"
   #return name,place
    print(f'name is{name}')
    print(f'place is{place}')
#print(details("anjum","HYD"))
#print(details("asma","asif"))
#print(details("ammi","abba",21))#raise typeerror as only 2 args taken
c,d=map(str,input("enter the value:").split(','))
details(c,d)

#defualt arguments-->we can make arguments as defualt but not first arguments
#as defualt
#def grocery(item,price=35):
#def grocery(item="cheese",price=100):#we can make all args default
#def grocery(item="cheese",price):#non deafult always follws default
    """usage od default arguments"""
    print(f'the item is {item} and the price is {price}')
grocery("milk",32)
#grocery(32,"milk")
grocery("bread")#it takes default pricee we have given
grocery("bread",45)
grocery()
'''
#keyword arguments-->whenever we want to specify the name of argument
def employee(name,salary,role,place="codegnan"):
    """keyword arguments usage"""
    print(f'employee name is {name} and salary is {salary} and role is {role},works in {place}')
employee("sai",20000,"admin")
employee(salary=25000,name="anjum",role="frontdesk")
employee("asma",40000,"IT","cognizant")
















































































