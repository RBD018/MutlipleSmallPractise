def comman_end(a,b):
    if len(a) and len(b) >= 1:
        if a[len(a)-1] == b[len(b)-1]:
            return True
        else:
            return False
    else:
        return False


a1 = list(input("Please enter the array to check: "))
b1 = list(input("Please enter the array2 to check: "))
print(comman_end(a1,b1))
