def sleepIN(weekday,vacation):
    if (weekday == False or vacation == True):
        return True
    else:
        return False

print('Please Enter true or false')
WeekDay = input("Enter is it weekday: ")
wkd1 = WeekDay.capitalize()
#if WeekDay == yes or WeekDay == Yes or WeekDay == 'Y':
#    WeekDay = True
#else:
#    print("Enter True or Yes ")
vacation = input("Enter if it is vacation ")
vc1 = vacation.capitalize()
#if vacation == {'Yes','yes','y'}:
#    vacation = True
#else:
#    print("Enter True or Yes")
print(wkd1,vc1)
if (wkd1 == 'True' and vc1 == 'True') or (wkd1 == 'False' and vc1 == 'False'):
    print(sleepIN(wkd1,vc1))
else:
    print("Please enter True or False")
