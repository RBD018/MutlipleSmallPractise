def fibonacci(nums):
    cnt = 0
    n1 = 1
    n2 = 2
    while cnt < nums:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        cnt += 1

num = int(input('Please enter the digit how many terms :'))
fibonacci(num)
