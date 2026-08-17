'''
mapping-->dictionary-->collection of key value pairs used to store
related data-->JSON,APIs,database records
dict()-->data={}->data={key : value}
dictoinary is mutable,indexed through key,ordered,heterogenous
keys must be unique(int,str,float values)

details={}
print(type(details))
details={'id':'CGH3996',
         'Name':'anjum',
         'gender':'female',
         'age':21,
         'batch':'DA23','place':'HYD'}
print(details)
print(len(details))
#access the data from dictionary
#details[0]#keyerror

print(details.keys())
print(details['id'],details['Name'])
#if key name not matching or not found/invalid
#print(details['marks'])# keyError as marks is not present
details['marks']=[]
print(details)
print(type(details['marks']))
details['marks'].append(20)
print(details)
details['marks'].extend([20,30,40,50,60])
print(details)
#create a pair value of practice session
details['practice_session']=('tuesday','thursday','saturday')
print(details)
#accessing 3rd day marks of student
print(details['marks'][2])
#accesing 2nd day of practice_session
print(details['practice_session'][1])
details['MI']=('monday','wednesday','friday')
#operations-->mutable,indexing through key,membership
print('wednesday' in details)
print('MI' in details)#retrun true as key there
for i in details:
    print(i)#retrun keys one by one
    
for i in details.keys():
    print(f'key={i}')
    print(f'value={details[i]}')
    
for i in details.value():#returns from dictionary
    print(i)
for i in details.items():#key value pair in tuple
    print(i)
for key,value in details.items():
    print(f'key is {key}')
    print(f' value is {value}')

#update
details.update({'marks':[],
               'PS':('tuesday','thursday','saturday')})
print(details)
details['marks'].extend([30,40,50,60])
print(details)
#or another method
mark=list(map(int,input("enter the marks").split(',')))
details['marks'].extend(mark)
print(details)

print(details.keys())
print(details.get('Name'))
print(details.get('branch'))#return none
details.setdefault('branch','bcom')#if key is not present it insert into dict
print(details)
details['branch']='B.com'
print(details)
print(details.setdefault('Name'))
details.keys()
print(details.pop('branch'))#we need to mention key
print(details.popitem())#remove and return a key,value as a 2 tuple
del details['id']
print(details.keys())
details.clear()#remove all elements frim dict
print(details)
#fromkeys()-->create from other iterable(lists,tuples,sets,str)
data=['anum','hyd','python']
a=dict.fromkeys(data)#create a dict into key and value none
a['anum']=21
print(a)
c=dict.fromkeys(['CGH123','CGH234'],['code','gyan'])
print(c)
'''
#task: create a dict with your personal details similar to codegyan profile

profile={'Name':'Anjum',
         'ID':'CGH3996','batch':'DA-HYD-023',
         'DOB':'2005-03-17',
         'age':21,'gender':'female',
         'state':'telangana','no.':7981204721}
print("personel details",len(profile))
for key,value in profile.items():
    print(key,':',value)

profile.update({'college_Name':[],
                'degree_pass% ':[],
                'SSC_pass%':[],
                'INTER_pass%':[]})
profile['college_Name'].append(input("enter degree college name:"))
profile['degree_pass% '].append(int(input("enter marks")))
profile['SSC_pass%'].append(int(input("enter marks")))
profile['INTER_pass%'].append(int(input("enter marks")))
for key,value in profile.items():
    print(key,':',value)








































