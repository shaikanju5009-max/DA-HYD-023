#for loop score of batsman
'''
inning = list(map(int,input("enter the score").split(',')))
total_score=Boundaries=dotballs=0 
for i in inning:
    if i == 0:
        dotballs +=1
    elif i == 6:
        Boundaries +=1
    else:
        total_score +=1
print("dotballs:",dotballs)
print("Boundaries:",Boundaries)
print("total_score:",total_score)
'''
#mam solution
'''
inning = list(map(int,input("enter the score").split(',')))
total_score=Boundaries=dotballs=0 
for i in inning:
    total_score += i
    if i == 0:
        dotballs +=1
    elif i == 6 or i == 4:
        Boundaries +=1
    else:
        total_score +=1
print("dotballs:",dotballs)
print("Boundaries:",Boundaries)
print("total_score:",total_score)
'''
#while loop for phone password
'''
pattern = "5009"
max_attempt=5
current_attempt=0
while current_attempt<max_attempt:
    entered_pin=input("enter the pattern:")
    if entered_pin == pattern:
        print("unlock successfull")
    else:
        print("wrong pattern...")
        current_attempt +=1
else:
    print("your phone is locked after 5 attempts..")
'''
#ATM pin with while
'''
PIN= "5009"
max_attempt=3
current_attempt=0
while current_attempt<max_attempt:
    entered_pin=input("enter the pattern:")
    if entered_pin == PIN:
        print("unlock successfull")
    else:
        print("wrong pattern...")
        current_attempt +=1
else:
    print("your phone is locked after 3 attempts..")
    '''
#movies of sequences
movies = input("enter movie names:").split(',')
count = 1
for movie in movies:
    print(count,movie)
    count +=1






































