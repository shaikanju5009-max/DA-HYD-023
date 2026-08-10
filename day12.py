'''
string-->caseconversion,searching&finding,string sarch method,
replace,space removal

#searching,finding,replacing,joining...
a = 'Codegnan'
print(len(a))
print(min(a))
print(max(a))
b = a.index('e')#it retruns index position
print(b)
c=a.index('n')#it retruns first occurance
print(c)
d = a.index('n',6)#it retrun next occurance
print(d)
#e = a.index('n',8)#valueerror
#print(e)
#f = a.index('t')#valueerror
#print(f)
g=a.index('n',1,4)
print(g)
'''
#rindex-->retrun last occurance(repiting chr)
'''
a = 'Codegnan'
b = a.index('g')
print(b)
c = a.rindex('n')#here n is occuring in 7th index
print(c)
#e = a.index('n',8)#valueerror
#print(e)
'''
#count()-->it retruns the number of object repeting
'''
print('codegnan'.count('n'))
print('code'.count('w'))#it retrun o as we dont have
print('asdasfed'.count('a'))
'''
#find()--->first occurance but it avoid error retrun -1 if
# substring not found
'''
print('codegnan'.find('r'))#retruns -1 if not there
print('anjum'.find('j'))#find index or same
print('asma'.rfind('a'))
# the diff is find give-1 and index shows error

a = 'data'
print(len(a))
for i in a:
    print(a.count(i),a.index(i))
    '''
#replacing,splitting,joining(funtions)--->logic
#strings are immutable
'''
a= 'codegnan'
print(a.replace('g','s'))
print(a)
a=a.replace('g','s')
print(a)
print('fg#ja#df$AD#'.replace('#',' '))
print(a.replace('x','anjum'))
'''
#spliting
'''
a = 'code anjum data'
print(len(a))
b= a.split()
print(b)
print(len(b))
c='code,anjum,python'
d= c.split()
print(d)
e = c.split(','  )
print(e)
'''
#joining(iterable)-->concatenate any number of string
'''
a='code'
b='gnan'
print(a.join(b))
print(b.join(a))
print('#'.join('anjum'))
#print(a+b)
print(' '.join('anjum'))
'''
# striing testing methods (boolean)
#isalpha(),isalnum(),isdigit(),issupport(),islower()....
'''
a = 'codegnan123'
print(a.isalnum())#retruns true if it is alphanumeric else false
b='codegnan'
print(b.isalnum())
print(a.isalpha())#gives true only if alphabets
print('5009'.isdigit())
print('2345'.isnumeric())#this has upper edge(nums,fractions,romans)
print('codegnan'.startswith('c'))
print('codegnan'.startswith('g',4))
print('codegnan'.endswith('f'))
print('codegnan'.islower())
print('Codegnan'.isupper())
print('Codegnan Python'.istitle())
'''
#space removal-->strip() (removes leading and trailing spaces)
'''
a = 'codegnan'
print(a.strip())
b=input("enter the names:").strip().lower()
print(b)
'''
#zfill()-->filling with zeros as per given numeric string
print('123'.zfill(4))
#centre(),ljust(),rjust(),--->aligment of strings(check length and
#then modidy the width)
print('anjum'.center(8))
print('anjum'.center(8,'#'))
print('hai'.ljust(6,'#'))
print('hai'.rjust(6,'#'))
































































































