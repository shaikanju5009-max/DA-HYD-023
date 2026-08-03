
'''#reapetition statements(loops)--->for,while(for with else),(while with else)
#---->jumping statements -->break,continue,pass
'''
#loops-->loops are helpful for repetation (automative tasks)
#syntax for (for keyword)
#for keyword wiil be healpful to iterate over a sequence/range
'''
for <temp_var> in sequence/range:
statements..
'''#range(start,stop,step)
#by deafult range picke 0 as start value
'''
for i in range(10):#orange keyword and purpule function
    print(i)
    #above we got 10 iterators
    
for i in range(1,10):
   # if i>5:
      #  print(f'value of i is-->{i}')
      if i>5 and i%2 == 0:
          print(f' final value of i-->{i}')
          
#step-->interval
for i in range(1,10,4):
    print(f'these numberss--->{i}')

for i in range(-10,0,1):
    print(i)
    
#[]-->we generally lists
names=['anjum','asma','asif']
print(len(names))
for name in names:
   # print(name)
    #print(f'student name is-->{name}')
     if name == 'asma':
         print(f'student name is-->{name}
         
#calculate sum of 10 numbers
#first understand your input-->range(11)-->10 numbers
#secound understand your output-->sum(number)
#third we need to map the logic
result=0
for i in range(11):
   # print(i)
    #print(f'result is{i+i}')
   result=result + i
   print(f'now the result is {result}')
print(f'sum of 10 numbers is {result}')

result=0
for i in range(21):
    if i%2 ==0:
       # print(i)
        result=result + i
       # print(result) clear
print(f'sum of first 10 even nubers-->{result}')
'''
#result vairable-->longest_streak
work_log = [0,1,1,1,0,1,0]
longest_streak=0#target vairable
current_streak=0
for day in work_log:
    if day == 1:
        #print(day)
        current_streak = current_streak + 1
        if current_streak > longest_streak:
            longest_streak=current_streak
    else :
            current_streak = 0
print(f'longest_streak is -->{longest_streak}')
   


























    

























         
        

