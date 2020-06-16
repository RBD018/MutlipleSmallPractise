def rotate_left3(nums):
    return nums[1:] + [nums[0]]


ls1 = list(input("Please enter the list : "))
print(rotate_left3(ls1))
