'''
list,tuples...
'''
#index(),count(),copy(),sort(),reverse()
'''
details=['codegnan',7,2018,'hyderabad']
print(len(details))
print(details.index(7))
print(details.index('codegnan'))
details.extend([7,21,34,21])
print(details.index(21))
print(details.index(21,6))
print(details.count(21))
print(details.count('python'))#it return 0 as we dont have it

data=['anum','python','hyderabad','data']

for i in data:
    print(data.index[obj],':',obj)
    '''
#copy()-->shallow copy of the given collection
'''
new=data.copy()
print(new)
print(type(new))
print(len(new))
new[2]='agentic AI'
print(new)
print(data)
data.append('analysis')
print(data)
print(new)
new.extend(['2026'])
print(new)

data=[1,2,3,[4,5,6],7,8]
new=data.copy()
print(new)
new[3][2]='agents'#whenever we make changes in nested list orginal
#will also affect
print(new)
print(data)
new[1]='python'
print(new)
print(data)
'''
#sort
'''
marks=[13,-23,23,34,12,13]
print(marks)
marks.sort()
print(marks)#return in asending order
print(marks.sort())#returrn none
marks.sort(reverse=True)#return decending order
print(marks)
marks.append('anjjum')
marks.sort()#not possiable on str and int typeerror
print(marks)
marks.insert(2,'code')
marks.reverse()
print(marks)
print(marks[::-1])
'''
#type(),len(),mix(),min(),print()
#print(sorted('codegnan'))#returns list in ascending ord
#print(sorted(['code','17',3,4]))#raise error

#tuples-->tuples are indexed ,ordered,heterogenous,immutable collection
#dimension,coordinate,database record,we prefer () for tuple notation
'''
a=()
print(type(a))
print(len(a))
dimension = 1.5,2.5
print(dimension)
print(type(dimension))
'''
#operations-->indexing,slicing,striding,membership,merging,repetition
'''
course=('PFS','JFS',('DA','DS'),'AgenticAI',[100,9,4])

print(course[3][-2:])
#course[2]=23 tuples are immutable
course[-1].append('codegnan')#we can make any modifications in the list
print(course)
'''
# task:create a nested tuple as above and work on slicing,striding and
#list func
'''
days=('monday','wednesday',['tuesday','thursday','saturday'],'friday','sunday')
print(len(days))
print(days[1][::3])
print(days[2][1][:5])
days[-3].append('holiday')
print(days)
days[2].extend(['practice'])
print(days)
#days.insert(2,'workingday')#attributeerror
#print(days)
'''
#complete task
'''
print('PFS' in course)
d=course*2 #repetation
print(d)
e=course+(2,3,4,5)#mearging
print(e)
#tuple immutable-->count(),index()
print(course.index('AgenticAI'))#return first occurance
print(course.count('agent'))
#print(course.sort())attributeerror -->sort()in list not in tuple
print(sorted(course[-1]))
#print(sorted()) as we have mix of str and int
#typecasting
d=tuple(sorted((23,34,45,56)))
print(d)
'''
#accept the grp of integer space sperated
'''
a,b=map(int,input('enter the values').split())
print(a,b)

a=tuple(map(int,input('enter the values').split(',')))
print(a)
print('9+2')
#eval() function can take any kind of input
print(eval('9+2'))
a=eval(input("enter the list:"))
print(a)
print(type(a))
#task:take a user input as string ,do this in two ways

1) give the count of each repeating character
test case1:programmig
output
r is reapeting 2 times
g is reapeting 2 times
m is repeting 2 times
'''
#task 1)
'''
name=input("enter the value:")
char=list(name)
unique=[]
for i in char:
    if i not in unique:
        count=name.count(i)
        if count>1:
            print(i,"is repeating",count,"times")
            unique.append(i)
            '''
#task 2)
name=input("enter the string:")
char=list(name)
unique=[]
for i in char:
    if i not in unique:
        count=name.count(i)
        if count>1:
           index=[]
           start=0
           for j in range(count):
               idx=name.index(i,start)
               index.append(idx) 
               start = idx + 1
            print(i,"is repeating" ,count," times")   
            print("index=",index)
        unique.append(i)
            










            











































































































