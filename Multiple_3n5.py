def multiple3n5(num):
    intarr = 0
    for i in range(1,num):
        if i % 3 == 0 or i % 5 == 0:
            intarr = intarr + i
            print(i,intarr)
    return intarr

nums = int(input("Enter the number you want to check the sum of multiples of 3 an 5:   "))
print("The number that are multiple of 3 and 5 below {} is {} ".format(nums,multiple3n5(nums)))
