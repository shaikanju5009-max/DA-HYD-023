'''
sequences-->string,lists,tuples,sets,frozenset
mapping-->dictonary
'''
#sets-->is a unique collection of objects,unordered,mutable,
#hashing,unindexed,heterogenous
#set(),{}
#a={} empty dict
'''
a=set()
print(type(a))
stud_id={123,234,345,456,234}
print(stud_id)#in unordered way 
print(type(stud_id))
#print(stud_id[2])# not in order so in order index typeerror
print(234 in stud_id)#membership allowed
#print(stud_id *2)#typeerror not allowed in set its unique
'''
#cannot merge or repeated arthematic operandans not possiable
'''
data={12,3,4,5,(12,3,4),'anjum'}

print(data)#no list inside a set (hashing technique) list are mutable
print(len(data))
for i in data:
    print(i)
    '''
#methods on sets -->add(),update(),remove(),discard(),pop()

name={'anjum','codegnan','hyderabad','data'}
'''
print(len(name))
name.add('analytics')# it insert a single element into it
print(name)
name.add(('python','appitude'))
print(name)
#name.insert(2,'sql')#attribute error
#print(name) insert not possiable in sets
'''
#update multiple elements and set into another set
'''
name.update(data)
print(len(name))
print(data)
data.update(name)
print(len(name))
print(len(data))
'''
#remove(),discard(),pop(),clear()
#remove() remove an element from the set(it must be an member)
'''
name.remove('anjum')
print(name)
#name.remove('anjum')#keyerror
#discard() will remove an element if its present else it ignore
name.discard('anjum')
'''
#pop()clear()
'''
name.pop()
print(name)
print(name.pop())#remove and return an arbritrary element
print(name.clear())#none output
name.clear()
print(name)#set() output
name.add('asma')
print(name)
name.update(('python','data'))
print(name)
'''
#copy
'''
a=name.copy()
print(a)
a.update({'asma','asif'})
print(a)
print(name)
'''
#mathematical operations-->union(),intersection(),difference(),symmetric
#issubset(),issuperset(),isdisoint()

da_23={12,34,45,54,32,12}
da_24={12,23,35,45}
'''
event=da_23.union(da_24)#retrun a new set from the set of other
event=da_23 | da_24 # .union() can be as |
print(event)
print(len(event))
common=da_23.intersection(da_24)#return the no of item in container
common = da_23 & da_24#7& for .intersection
print(common)
print(len(common))

common = da_23.intersection_update(da_24)
print(common)#it retrun none
print(da_23)#common elements are finnally sorted
'''
print(da_23)
print(da_24)
#difference remove common elemnts and print diiff elements
'''
diff=da_23.difference(da_24)
print(diff)
f=da_23-da_24
print(f)
'''
#symmetric_difference-->remove common elements and print all remg
#elments from two sets
'''
symm=da_23.symmetric_difference(da_24)
print(symm)
h=da_23^da_24
print(h)
'''
#issubset-->checks for all elements to be present in other set
'''
da_24.remove(35)
da_24.remove(23)
print(da_24.issubset(da_23))
print(da_23.issuperset(da_24))
#isdisjoint() returns false for set having common elements
print(da_23.isdisjoint(da_24))
'''
#length of unique

n=int(input())
student_id=input().split()
result=set(student_id)
print(result)
print(len(result))


































































