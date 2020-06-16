def sum3(nums):
    sums = 0
    for i in nums:
        sums = sums+int(i)
    return sums

ls1 = input("Enter the array to sum: ")
print(sum3(ls1))
