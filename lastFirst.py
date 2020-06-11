def lastFirst(str1):
    print (str1[-1]+str1[1:len(str1)-1]+str1[0])

a = True
while(a):
    s1 = input('Input the word where first letter will be interchanged with the last one : ')
    lastFirst(s1)
    Again =  input('Do you want an another word to try (Y/N)')
    if Again == 'Y' or Again == 'y':
        a = True
    else:
        a = False
        break
