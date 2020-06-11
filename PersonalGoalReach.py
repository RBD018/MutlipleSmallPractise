flag = True
while flag:
    startingAmount = float(input("Enter the current ammount in your bank ? "))
    goalAmount = float(input("Enter your goal amount ?"))
    rateOfIntrest = float(input("Enter the rate of interest"))
    calculateAmount = startingAmount
    year = 0
    a = True
    while a:
        if calculateAmount <= goalAmount:
            interestAmt = calculateAmount*(rateOfIntrest/100)
            calculateAmount = calculateAmount+interestAmt
            #print(calculateAmount)
            year = year +1
        else:
            a = False
            break
    print("it will take you {} years to reach your {} ammunt".format(year,goalAmount))
    b = input("Do you want to try the new test case (Y/N) ")
    if b == 'N':
        break
    else:
        flag = True
