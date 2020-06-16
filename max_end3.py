def max_end3(nums):
    ln = len(nums)
    if int(nums[ln-1]) > int(nums[0]):
        for i in range(0,ln):
            nums[i] = nums[ln-1]
        return nums
    else:
        for i in range(0,ln):
            nums[i] = nums[0]
        return nums

ls1 = input("Please enter the list to check and fill with biggest number seperate by comma: ")
ls1 = list(ls1.split(','))
print(max_end3(ls1))
