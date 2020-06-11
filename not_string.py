def not_string(str1):
    if len(str1)>=3 and str1[:3] == 'not':
       print (str1)
    else:
        print ("not "+ str1)

str2 = input('Enter the string: ')
not_string(str2)
