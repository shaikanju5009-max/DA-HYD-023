'''
sequences-->strings,lists,tuples,sets
mapping-->dictinory
'''
#lists-->collection of heterogenous elements
#lists-->indexed,ordered,mutable,heterogenous,we use [] to store the data
'''
marks = [35,34,36,37]
print(marks)
print(len(marks))
print(type(marks))
print(37 in marks)
'''
#operations : indexing,slicing,striding,membership,merging,reptitions
#nested lists-->a list inside another list
'''
names = ['codegnan',25,24.70,[23,34,45,56],'da023',34]
print(len(names))
print(names[0])
print(names[3])
print(type(names))
print(names[0][:4])
print(names[0][4:])
print(names[0][::2])
names[0]=names[0][::-1]
print(names)

print(names[3])
print(len(names[3]))
print(names[3][2])
names[2]='python'
print(names)
#by indexing if we change the elements,lengths of collection will remain same
names[4]=['anjum','data','analysis']
print(names)
print(len(names))
print(names[3][1:3])
print(names[4][0][4:])

names[2:4]='asma','asif','mom','dad'
print(names)
#in slicing whatever elements u pass as per the logic length keeps on increace
names[3:6:2]='python','java'
print(names)
'''
#create a nestetd list with strings,lists and work on indexing,slicing,striding
#added advantage if u could add string functions also to it
'''
names = ['apple','banana',['cat','dog'],'flower','rose',[17,13,15]]
print(type(names))
print(len(names))
print(names[2])
print(names[5][0])
print(names[2][0][:4])
print(names[3][::2])
print(names[1].upper())
print(names[2].count('cat'))
'''

#lists functions-->append(),insert(),extent(),pop(),remove(),clear()
#index(),count(),copy(),sort(),reverse()
'''
names=['codegnan','anjum']
names.append('data')
#print(names)
#names.append('analysis','agents')#typeerror
names.append(['analysis','agents'])
#print(names)
#append() will always increment the length of list by 1
#print(names[3].append('chatgpt'))# it returns none as append is
#applicable on list not on print
print(names)
#extend()-->inserts multiple elements to the end of list

names.extend('analysis')#string will be splitted
print(names)
names.extend(['analysis'])
print(names)
names.extend([12,23,34,45])
print(names)
#names.extend(12,23)#typeerror
#print(names)
'''
#insert(index,object)-->insert object before index
'''
names.insert(1,'python')
print(names)
#names.insert([1:4],['a','bn'])#syntax error accept only index not slicing
#print(names)
names.insert(-1,'aaa')
print(names)'''
#task-->list into sequence
data=['anjum','data','analysis','python']
for i in range(len(data)):
    print(f'{i}={data[i]}')








































































