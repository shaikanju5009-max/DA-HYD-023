'''
functions--->vairable length arguments(*args)
        --->keyword vairable length arguments(**kwargs)

vairable length arguments-->the number of positional arguments are not limit
we can pass any number of positional arguments, but we need to use the * represention,
data is stored in tuple.

def sample(*args):
    """simple demo for *args"""
    print(args)
    print(type(args))
sample()#no arguments
sample(1,2,3,4)#any number
sample("codegnan",'anjum',21)
details=[12,23,34]
sample(details)#passing a collection
sample(*details)#unpacking values from collection
'''
'''
a,b,c="anjum",21,"python"
print(a,b,c)
#a,*b,c="data","analysis",23,"HYD",5,"codegnan"
a,b,*c="data",21
print(a)
print(b)
print(c)
c.extend([5,"python"])
print(c)
'''
#task-->we wanted to calculate the sum of given objects using function
'''
def add(*a):
    """sum of given objects"""
    print(a)
    print(type(a))
    #take vairable output as result
    result=0
    for i in a:
        #print(i)
        #if type(i) == int or type(i) == float:
        if type(i) in (int,float,complex):
            result=result + i
    return result
#print(add())
#print(add(12,3,45,6))
#print(add(12,4,34,4.5))
#print(add(3,4,5,"poll",4.5))
#print(add(3,4,5,2+3j,"poll",4.5))
b= list(map(int,input("enter the values").split(',')))
print(add(*b))#* is used to unpack the value from the collection
print(b)
print(*b)#it returns each value side by side
for i in b:
    print(i,end=' ')#same as here using loop
    '''
#keyword vairable length arguments-->we can pass any number of keyword
#arguments we use ** representation data is stored in dictionary
'''
def details(**kwargs):
    """usage of **kwargs demo"""
    print(kwargs)
    print(type(kwargs))
details()#return empty dict
details(name="codegnan",place="kukatpally",batch="DA")
batch={'number':'da23','age':21}
details(**batch)
'''
#now let us include both of them into a function
'''
def sample(*a,**b):
    """usage of both lengt and keyword vairable length args"""
    result=0
    for i in a:
        if type(i) in (int,float,complex):
            result = result+i
    print(result)
    for key,value in b.items():
        print(f'key is {key}')
        print(f'value is {value}')
sample(2,4,6,"anjum","DA",4.5,
       name="anjum",
       place="HYD",
       batch="DA23")
       '''
#sample(name="anjum",23,ids=2345)positional args follow keyword args
#retrun give use printin arguments
#if print given in loop then arguments give function call

#1)student grade calculator
'''
def calculate_grade(marks):
    """grade calculator """
    if marks >= 80 and marks<=100:
        return "A"
    elif marks >= 60 and marks<=79:
        return "B"
    elif marks >= 40 and marks<=59:
        return "C"
    else:
        return "Fail"
        
for i in range(3):
        marks=int(input("enter the marks {}:".format(i+1)))
        grade= calculate_grade(marks)
        print("Marks:",marks,"Grade:",grade)
        '''
#2)shopping bill calculator
'''
def calculate_bill(price,quantity=1,discount=0):
    """calculate bill """
    total=price*quantity
    dicount= (total *discount)/100
    final_bill = total - discount
    return final_bill
print("Bill1",calculate_bill(100))
print("bill2",calculate_bill(100,2))
print("bill3",calculate_bill(price=100,quantity=2,discount=10))
'''
#3)BMI calculator
'''
def calculate_bmi(weight,height):
    """calculate bmi"""
    bmi=weight/(height **2)
    return bmi
def bmi_status(bmi):
    """return BMI category"""
    if bmi < 18.5:
        return "Underweight"
    elif bmi >=18.5 and bmi <=24.9:
        return "Normal"
    elif bmi >=25 and bmi <=29.9:
        return "overweight"
    else:
        return "obese"
for i in range(3):
    print(f'enter the details for person {i+1}')
    name=input("enter the name:")
    weight=float(input("enter the weight in kgs:"))
    height=float(input("enter the heights in meters:"))
    bmi=calculate_bmi(weight,height)
    category=bmi_status(bmi)
    print("Name:",name,"BMI",round(bmi,2),"category:",category)
    print()
    '''
#4)marks summary using *args
'''
def marks_summary(*args):
    """vairable length *args"""
    total=0
    if len(args) == 0:
        return 0 ,0
    for mark in args:
        total += mark
    avg = total/len(args)
    return total,avg
t1,a1=marks_summary(80,90,70)
print("total:",t1,"avg:",a1)
t2,a2=marks_summary(100)
print("total:",t2,"avg:",a2)
t3,a3=marks_summary()
print("total:",t3,"avg:",a3)
'''
#5)employee details using **kwargs
def display_employee(**kwargs):
    """keyword vairable task"""
    for key,value in kwargs.items():
        print(f'{key} : {value}')
    if "salary" in kwargs:
        print("salary info:available")
    else:
        print("salary info : not provided")
    if "department" in kwargs:
        print("department info:available")
    else:
        print("department info : not provided")
    print()
display_employee(name="anjum",age=21,salary=50000,department="IT")
display_employee(name="anjum",age=21,salary=50000)
display_employee(name="anjum",age=21,department="IT")
    
        
        
    



























































        
    










































