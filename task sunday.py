#grade checker--->useing if-elif-else conditional chain
'''
marks = int(input("enter the marks:"))
if marks>=100:
    print("invalid marks")
elif marks>=90:
    print("grade: A")
    print("remarks: outstanding!")
elif marks >=80 and marks <=89:
    print("grade: B")
    print("remarks: excellent!")
elif marks >=70 and marks<=79:
    print("grade: C")
    print("remarks: good!")
elif marks >=60 and marks <=69:
    print("grade: D")
    print("remarks: fair,needs improvement!")
elif marks >=50 and marks >=59:
    print(" grade: E")
    print("remarks: poor,needs serious improvement")
elif marks<50 and marks >=0:
    print(" remarks:FAILED,need to reappear")
else:
    print("no -ve values")
'''
#even-odd cheaker(with twist)
'''
num=int(input("enter the numbers:"))
if num == 0:
    print("zero is neither even nor odd")
elif num <0 and num % 2 == 0:
    print("negative even numbers")
elif num <0 and num % 2 != 0:
    print("negative odd number")
elif num >0 and num % 2 == 0:
    print("even number")
else:
    print("odd number")
'''
#season identifier---->(if-elif-else)
month=int(input("enter month number:"))
if month <=1 and month >=12:
    print("invalid month entered")
elif month == 12 or month==1 or month==2:
    print("season: WINTER")
elif month ==3 or month==4 or month==5:
    print("season: SPRING")
elif month==6 or month==7 or month==8:
    print("season: SUMMER")
elif month==9 or month==10 or month==11:
    print("season: AUTUM")
else:
    print("invalid month entered")

























