'''
exeption handling / scope of vairable / built-in functions
exeption handling -->it is a mechanism that hepls to respound or make the
flow of execution in normal way,without this errors will occur and disrup
the flow of program

common exeption-->value error,typeerror,index error,attributeerror,
zero division error..
syntax:
try:
    #code that will cause the exception
except Exception as e:
    #code will catch the exeption
finally:
    #runs irrespective of try/except...
    ...
'''
#basic Exeption handling
'''
try:
    #a = 10
    a= (int,input("enter the value:").split(','))
    #result = 20/a
    print(a[5])
    #print(resul)#check for nameerror
#except Exception as e:
#    print(e)#it returns the msg of error
except ValueError:#check by changing case(valueerror)
    print(f'Invalid entry only integer values')
except ZeroDivisionError:
    print(f'Division by zero is not possiable')
except NameError:
    print(f'check the name of vairable properly')
except IndexError:
    print(f'no index found')
    '''
#similarly if we want to check other errors-->IndexError,AttributeError,
'''
try:
    a=[10,20.30]
    print(a[5])
except Exception as e:
    print(e)#return the msg of error
except IndexError:
    print(f'checknleng of list')
except AttributeError:
    print(f'dont rush write name properly')
    '''
#handling exception at a time
'''
try:
    a=[10,20,30]
    a.append([24])
    print(a[5])
except(IndexError,AttributeError) as e:
    print(e)
    a=list(map(int,input("enter the value:").split(',')))
    print(a)

while True:
    try:
        weight = int(input("enter the weight in kgs:"))
        height = float(input("enter the height in metrs:"))
        #write my logical condition
        if weight > 0 and height > 0:
            break#stops the flow of execution
            #countinue skips the current iteration nad proceeds for rmg iteam
        else:
            print("make sur to enter the corect values")
    except ValueError:
        print(f'make sure to enter weight as integer only,height is also in number')
bmi=((weight)/(height)**2)
print(bmi)
'''
#use Exception handling along with jumping statements in
#functions BMI task


#scope of vairable-->scope is basically the region/area where it is
#accessible
#local scope,globa scope
#global keywords,enclosing scope(nested function nonlocal keyword)
'''
local scope-->vairable defined inside the function accessible inside

def display():
    """usage of local scope"""
    name="codegnan"#local vairable
    print(name)
display()
print(name)#nameerror
'''
#global scope(vairables)-->defined outside and can be asscessible anywhere
#in the script
'''
place="HYDERABAD"#global vairable
def display():
    """usage of local&global scope"""
    name="codegnan"#local vairable
    print(name)
    print(f'{name} is in {place}')
display()
print(place)
'''
#modifiying global vairable inside the function and accessible outside the function
'''
count = 20
def data():
    """usage of global keyword"""
    global count
    count = count + 5
    print(f'value inside function is {count}')
data()
print(f'value outside function is {count}')

'''
#local vairable has high priority over global vairable
'''
count = 20
def data():
    """proiority of local vs global vairable"""
    count = 5
    count = count + 5
    print(f'value inside function is {count}')
data()
print(f'value outside function is {count}')
'''
#enclosing scope(non local keyword)
def outer():
    """outer function with local vairable"""
    count = 5
    def inner():
        """nested function"""
        nonlocal count
        count = count + 10
        print(f'value inside is {count}')
    inner()
    print(f'value outside is {count}')
outer()
    
#built in functions-->vairable buitinscope
len = 56
print(len+4)
print(len('codegnan'))#typeerror--> never ever use builtin function as identifiers
#it is acting as vairable















































































            



























