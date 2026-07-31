'''
identity operators-->id()

a=5
b=a
print(id(a))
c=5
print(c is a)

a= [1,3,5,6]
b=a
print(id(a))
c=[1,3,5,6]
print(id(c))
#as we have list(mutable collection) both c,a have list different
#ids values are same
print(c is a)
print(c == a)
print(a is not c)

# bitwise operations--> we perform over operands
#&(and),|(or),^(XOR),shifting(<<,>>)
a=5&3
print(a)#both 5 and 3 to be converted binary and bitwise & is performed
print(5|3)#(| or)
print(5^3)#(^ XOR)
print(5 and 3)

#leftshift operator <<, rightshift>>
#print(5<1) false (comparision)
print( 5 << 1)# leftshift operation by 1 position 
print(5>>1)
print(15<<2)# covert 15 binary and perform 2 times left shift
print(15>>2)

#input formatting-->
#you know single input

names = input("enter the names:").split(',')
print(names)
name1,name2=map(str,input("enter:").split(','))
print(name1,name2)
'''
#control block statetment-->they control the flow of programm
#when to execute,how to excute
#conditional statements-->if,else,elif(rely on condition to be executed)
#repetition statements(loop)-->for,while
# conditional -->if usage
'''
syntax:
if<condition>:
statements(s).......
..

#age=15
age=int(input("enter the age:"))
if age >=18:
    print('your age is',age)
    
age=int(input("enter the age:"))
if age >=18 and age in[19,21,22]:
    print('your age is',age)
    '''
#else keyword --->if-else
'''
sytax-->
if <condition>:
     statements(s)......
else
     statement(s).....
     '''
#vote elgibility--> to check her elgibility and give access
'''
age=int(input("enter the age:"))
if age>=18:
    print("you have voter elgibility and age is",age)
    print("access granted")
else:
    age = 18-age
    print(" you dont have elgibility",age,"years")

'''
#some cases lets use only nested--->if,else
'''
age=int(input("enter the age:"))
if age>0:
    if age >=18:
        print("you have voter elgibility",age)
        print("access granted")
    else:
        age = 18-age
        print("you need to wait for more",age,"years")
else:
    print("you have entered -ve value/zero enter only +ve ")
'''
marks=int(input("enter the marks:"))
if marks>=0 and  100:
    if marks >=90:
        print("your grade is  A")
    else:
        if marks >=80:
            print("your grade is B")
        else:
            if marks >=70:
                print("your grade is C ")
            else:
              if marks >=60:
                  print("your grade is D")
              else:
                 print("FAILED")
else:
    (" -ve is not allowed and not more than 100 ")
                
                
         











    
        
        
    
    

    


















            









































    































