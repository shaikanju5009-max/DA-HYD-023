#elif condition-->
'''
syntax
if <condition1>:
statement
elif<condition2>:
statements
elif<condition3>:
statements
else:
statements

marks = int(input("enter the marks:"))
if marks>=100:
    print("ener the values should be greater then 1 and less than 100")
elif marks>=90 and marks <=100:
    print("grade A")
elif marks >=80 and marks <=89:
    print("grade B")
elif marks >=70 and marks<=79:
    print("grade C")
elif marks <=60 and marks <=69:
    print("grade D")
elif marks <60 and marks >=0:
    print(" your FAILED ")
else:
    print("no -ve values")
  '''  
#task use same in another way
light=input("chose the traffic colour: ")
if (light == "red"):
    print("stop dont cross the limit")
elif(light == "yellow"):
    print("wait ,ready to go")
elif(light == "green"):
    print("you can GO")
else:
    print("light is broken ,not exits")
    
'''
age=int(input("enter the age:"))
if age>=18 and age<=100:
    print("-------user has the vote elgibility--------")
    print("----acces granted----")
elif age<18 and age>0:
    print("--user has no elgibility--- ")
    print("use has to wait for more",(18-age),"years")
else:
    print("--only +ve values and less than 100 allowed")
    
# output formatting-->old style formatting
a=5
b=10
print(a,b)
print(a,b,sep=',')
name="codegnan";batch="dataAnalysis"
print(name,batch,sep=',')
print(name ,batch,sep="---------->")
print (name,batch,end='\t')
print(a,b,end=',')
print("HYD")

'''
name='codegnan';age=7;batch='DA-HYD-023';place='hyd'
'''
print(batch'is in'name)
#old style formatting--->%d(integer)%s(str),%f(float)
salary = 2345.456
print("his salary is %d"%(salary))
print("his salary is %f"%(salary))
print("his salary is %.1f"%(salary))

#.format() usage
print("{} is in {}".format(name,place))#order matters
#fstring usage more recomended
print(f'{name} is in {place}')
print(f'{"anjum"} is in {name}')

'''









































