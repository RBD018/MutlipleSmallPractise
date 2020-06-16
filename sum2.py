def sum2(nums):
  sums = 0
  ln = len(nums)
#  print(ln)
  if ln > 2:
#      print("True")
      sums = sums + int(nums[0]) + int(nums[1])
      return sums
  else:
#    print("False")
    for i in range(0,ln):
          sums = sums + int(nums[i])
    return sums

print("Sum of first two elements: ")
ls1 = str(input("Please enter the list seperated with comma ',': "))
l2 = ls1.split(',')
print(sum2(l2))
