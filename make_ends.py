def make_ends(nums):
    return nums[:1] + nums[-1:]


ls1 = str(input("Please enter the string with seperating them with a comma ',': "))
ls2 = ls1.split(',')
print(make_ends(ls2))
