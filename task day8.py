#slicing,striding-->string
'''
name = 'CodegnanAcademy'
print(len(name))
print(name[:4])
print(name[8:])
print(name[4:-1])
print(name[-15:-7])
print(name[::-1])#reverse the string
print(name[:16:2])
print(name[1:17:3])
'''
#print A to Z usage of loop
#print(ord('A'))
#print(ord('Z'))
letters = 65
while letters <= 90:
    print(chr(letters),end=' ')
    letters += 1
