'''
sequences-->string,list,sets,tuples,mapping(dict)
'''
#string--> group of characters,we use single or double or triple quotes
#for representing string
#strings are immutable,ordered,indexed collection
#space is also a character in len
'''
name = 'codegnan'
print(type(name))

print(len(name))#-->output in number of item in container
#index is used to fetch the object(position)start with 0 and end at len(obj)-1
#we use [] represention
print(name[0])
#print(name[25])#indexerror--->out of range
#negative index --->-1 to len(obj)
print(name[-1])#it retrun last character
#print(name[-33])indexerroe--->ot if range

#slicing-->we can access group of character(objects)
#we use [start:end] start deafult-->start is 0,end is exclude
print(name[:])#entire output
print(name[0:])#same output
print(name[:4])#start with 0 and end exlude 4
print(name[1:5])

name = 'anjum'
print(name[:6])#entrie
print(name[0:4])
print(name[7:3])#immutable  return empty
#slicing is applicable from lower index to higer index
print(name[:45])#retrun till end of string
'''
name = 'python'

#print(name[-1:-5])#immutable
print(name[-2:])
print(name[4:])
print(name[-4:-1])

print(name[1:-2])
print(name[2:-6])#immutable
'''
#observ +ve,+ve&,-ve,-ve& +ve,-ve al posibility

#striding--->[start,stop,step]
course = 'dataAnalysis'
print(len(name))
print(course[:4])
print(course[4:])
print(course[-3:])
print(course[::2])#includes start to end skkipinf 1 character
print(course[1:6:3])#[1:6]-->ataAn-->[1:6:3]-->aA
print(course[2::3])
print(course[::-1])#it retrun the reverse of the string
print(course[::-2])
'''
#task workout with all posibilityies of slicing and striding on a example
'''
name = 'codegnan'
#name[3] = 'w'#strings are immutable
#operations on string--> indexing,concatenation,repetiton,membership
print(name * 3)
print('*' * 25)#reptition
#concatenation-->combining string
data = 'anjum' + 'python' + ' ' + 'database'
print(data)
print('121' * 4)#numeric string
print('code' in 'codegnan')#membership

for i in 'codegnan':
    print(i,':')
    #we get everything in line by line
for i in 'codegnan':
    print(i,end=' ')

#built-in function-->len(),min(),max(),sorted()
name = 'dataCodegnan'
print(len(name))
print(min(name))#alphabetic order ASCI ordering
print(ord('A'))#ASCI value
print(ord('a'))
print(chr(97))
print(max(name))
print(sorted(name))#returns a list by sorting all elements
'''
'''
#methods on string-->case--converstion,finding/searching
name = 'codegnan data'
#case--conversion-->upper(),lower(),title(),captalized()
a = name.upper()
print(a)
b = name.lower()
print(b)
#capitalize()-->converts first letter to uppercase
c = name.capitalize()
print(c)
d = name.title()#covert every word first letter to uppercase
print(d)
'''
#task : a to z
#use loops and string to return a-z





































































