'''
price = list(map(int,input("enter the price:").split(',')))
total = 0
for i in price:
    total= total +i
print(f'sum of 4 iteams is--->{total}')

#password analyser
password = input("enter the password:")
upper=lower=digit=special=0
for ch in password:
    if 'A'<=ch<= 'Z':
        upper +=1
    elif 'a'<=ch<='z':
        lower +=1
    elif '0'<=ch<='9':
        digit +=1
    else:
        special +=1
print("upper:",upper)
print("lower:",lower)
print("digits:",digit)
print("special:",special)
'''
mail=input("enter email:".split(','))
for i in email:
    print(mail.split('@')[1])
