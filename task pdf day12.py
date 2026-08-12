#text case convewerter
'''
a = input('enter a sentence: ')
print('\n-------different case converter--------\n')
methods = ["upper","lower","title","capitalize","swapcase","casefold"]
for method in methods:
    if method =="upper":
        result = a.upper()
    elif method =="lower":
        result = a.lower()
    elif method =="title":
        result = a.title()
    elif method =="capitalize":
        result = a.capitalize()
    elif method =="swapcase":
        result = a.swapcase()
    elif method =="casefold":
        result = a.casefold()
    print(method.capitalize() + ":",result)      
print('checking orginal'.center(8,'*'))
if a.isupper():
    print("orginal is uppper:")
elif a.islower():
    print("orginal is lower:")
elif a.istitle():
    print("orginal is title:")
else:
    print("orginal is mixed")
    '''
#username validator
'''
name = input("enter username:")
count = 0
while name != "quit":
    count +=1
    if name.isalnum():
        print("username contains only letters and numbers")
    elif name.isalpha():
        print("username begins with letter")
    elif name.isidentifier(): 
        print("valid python identifier ")
    elif name.isascii():
        print("contains only ASCII character")
    if name and name[0].isalpha():
        print("begins with a letter")
    else:
        print("does not contain only letters and numbers")
    name = input("enter the username:")
else:
    print("exiting.....")
    '''
#formatted student report
'''
print("STUDENT REPORT".center(50))
name_header = "Name".ljust(15)
marks_header = "Marks".rjust(10)
grade_header = "Grade".rjust(10)
print(f'{name_header}{marks_header}{grade_header}')
students = [
            ["anjum",85],
            ["asma",75],
            ["asif",65],
        ]
for student in students:
    name = student[0]
    marks = student[1]
    if marks>=80 and marks<=100:
        grade = "A"
    elif marks>=60 and marks<=79:
        grade = "B"
    elif marks>=40 and marks<=59:
        grade = "C"
    else:
        grade="Fail"
    name_col = name.ljust(15)
    marks_col = str(marks).rjust(10)
    grade_col = grade.rjust(10)
    print(f'{name_col}{marks_col}{grade_col}')
    '''
#character and text analyser
text = input("enter a line of text:")
letters = 0
digits = 0
spaces = 0
printable = 0
non_printable = 0

for ch in text:
    if ch.alpha():
        letters += 1
    if ch.isdigit():
        digits += 1
    if ch.isspace():
        spaces +=1
    if ch.isprintable():
        printable +=1
    else:
        non_printable += 1
print("letters:",letters)
print("digits:",digits)
print("spaces:",spaces)      
print("printable:",printable)
print("non_printable:",non_printable)
print("lower case:",text.islower())
print("upper case:",text.ispper())
print("title case:",text.istitle())






















        
















        

       
 
        
    
        
        
        









