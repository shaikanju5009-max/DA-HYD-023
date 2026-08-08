#guesss the pin
'''
secret = 5009
guess = int(input())
while guess != secret:
    if guess < secret:
        print("your low")
    else:
        print("too high")
    guess = int(input())
print('correct gjava
javauess....')
'''
#otp verification
'''
otp = "121"
max_attempt = 7
current_attempt = 0
while current_attempt<max_attempt:
    entered_pin=input("enter otp")
    if entered_pin == otp:
        print("otp verified")
    else:
        print("not valid")
        current_attempt +=1
else:
    print("not more than 7 attempt..")
    '''
#food bill
'''
food = input("enter the items:")
count = 0
while food != "exit":
    count +=1
    food = input("enter item:")
print("total no.of ordered items..:",count)
'''
#win the game
secret = "python"
current_attempt = 3
while current_attempt>0:
    entered_pin=input()
    if entered_pin == secret:
        print("you won the match")
    else:
        current_attempt =current_attempt-1
        print("you have",current_attempt,"more chances")
else:
    print("you lost the game")
























    
        
        
