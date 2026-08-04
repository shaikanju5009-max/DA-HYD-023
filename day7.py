'''
usage of else with for-->the else keyword will only be executed when the loop is
'''
#for with else
'''

work_log = [0,1,1,1,0,1,0]
longest_streak=0#target vairable
current_streak=0
for day in work_log:
    if day == 1:
        #print(day)
        current_streak = current_streak + 1
        if current_streak > longest_streak:
            longest_streak=current_streak
            print(longest_streak)
    else :
            current_streak = 0
else:
    print(f'longest_streak is -->{longest_streak}')
    '''
    # in this loop the entrie loop execution is done we get result of
    #else block
'''
work_log = [0,1,1,1,0,1,0]
longest_streak=0#target vairable
current_streak=0
for day in work_log:
    if day == 1:
        #print(day)
        current_streak = current_streak + 1
        if current_streak > longest_streak:
            longest_streak=current_streak
            print(f'longest_streak is {longest_streak}')
            break
    else :
            current_streak = 0#streak break
else:
    print(f'longest_streak is -->{longest_streak}')
print("execution done")
'''
#for else with notification scenario
'''
notifications =[0,0,0,1,0]
for notification in notifications:
    if notification == 1:
        print('unread notification')
        break
else:
    print('all caught up')
'''
#try to take notification from user-->list of int
'''
notifications =list(map(int,input("enter the values-->0 or 1:").split(',')))
print(notifications)                    
for notification in notifications:
    if notification == 1:
        print('unread notification')
        breakc
else:
    print('all caught up')
    '''
#while-->it return on condition ,it will completely execute until the
#condition is satisfied
'''
syntax
while<condition>:
statement;;;;

while True :
    print('yes')
    
#it run an infinite loop we need to press crtl+C(keybord interrupt)
i =10
while i>=1:
    print(i)
    i=i-1#decrement i-1
    '''
#banking scenario-->pin authentication if more than 3 attempts
#account locked
pin="5009"
max_attempt=3
current_attempt=0
while current_attempt< max_attempt:
    entered_pin =input("enter the ATM PIN:")
    if entered_pin == pin:
        print("login sucessful")
        break
    else:
        print("enter pin is wrong...try again carefully")
        current_attempt +=1
else:
    print("account locked...try after 24hours....")
    

























    


















