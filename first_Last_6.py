def first_last_6(nums):
    if nums[0] == '6' or nums[len(nums)-1] == '6':
        return True
    else:
        return False

list1 = list(input('Please enter the numbers you want to check: '))
print(list1)
print(first_last_6(list1))

