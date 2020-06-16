def has23(nums):
    for i in nums:
        print(i)
        if int(i) == 3 or int(i) == 2:
            return True
    return False

ls1 = str(input("Enter the list with commas(',') as seperated and check if 2 and 3 are available:   "))
ls2 = ls1.split(',')
print(has23(ls2))
