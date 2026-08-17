#student marks buit and updated
'''
marks=[]
for i in range(3):
    mark=int(input(f'enter the marks {i+1}:'))
    marks.append(mark)
marks.insert(0,90)
marks.extend([75,85])
print(marks)
if 75 in marks:
    marks.remove(75)
    print(marks)
removed_value=marks.pop()
print("removed value:",removed_value)
print("final list:",marks)
print("length of marks:",len(marks))
'''
#number list analyser
'''
nums=[20,10,30,20,40,20]
nums.sort()
print("Ascending order:",nums)
nums.reverse()
print("Descending order: ",nums)
search_num=int(input("enter the number:"))
if search_num in nums:
    print("number found!")
    print("Count:",nums.count(search_num))
    print("first index:",nums.index(search_num))
else:
    print("number not found in list")
print("Smallest value:",min(nums))
print("largest value:",max(nums))
print("total sums:",sum(nums))
'''
#even and odd number separator
'''
num=[10,15,20,25,30,35]
even=[]
odd=[]
for i in num:
    if i % 2 == 0:
        even.append(num)
    else:
        odd.append(num)
print("Even list:",even)
print("Odd list:",odd)
print("Frist three values:",num[:3])
print("Last three values:",num[-3:])
backup=num.copy()
print("Backup value:",backup)
num.clear()
print("Orginal list:",num)
print("backup list:",backup)
'''
#unique name manager
'''
names=["Asha","Rahul","Asha","John","Rahul"]
a=set(names)
print(a)
a.add("meera")
a.update({'Arun','Priya'})
print("the names added:",a)
if "John" in a:
    print("name found!")
    a.remove("John")
    print("after removing john:",a)
a.discard('David')
print("after discarding david:",a)
print("Final unique names:")
for i in a:
    print(i)
    '''
#course student comparision
python_students={'Asha','Rahul','John','Meera'}
da_students={'Rahul','Meera','Arun'}
print("python students:",python_students)
print("DA students:",da_students)
all_students=python_students | da_students
print("union:",all_students)
both_course=python_students & da_students
print("intersection:",both_course)
only_python=python_students - da_students
print("differnce:",only_python)
only_one=python_students ^ da_students
print("symmetric diffrence:",only_one)
is_subset=da_students.issubset(python_students)
print("subset:",is_subset)
superset=python_students.issuperset(da_students)
print("superset:",superset)
disjoint=python_students.isdisjoint(da_students)
print("disjoint:",disjoint)
print("students in python:")
for student in python_students:
    print("-",student)
print("students in DA:")
for student in da_students:
    print("-",student)












































































