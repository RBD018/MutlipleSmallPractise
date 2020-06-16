def middle_way(a,b):
    lna = int(len(a)/2)
    lnb = int(len(b)/2)
    if len(a) % 2 == 0 and len(b) % 2 == 0:
        c = [0,0,0,0]
        c[0] = a[lna-1]
        c[1] = a[lna]
        c[2] = b[lnb-1]
        c[3] = b[lnb]
        return c
    elif len(a) % 2 != 0 and len(b) % 2 != 0:
        c=[0,0]
        c[0] = a[lna]
        c[1] = b[lnb]
        return c
    else:
        if len(a) % 2 == 0 and len(b) % 2 != 0:
            c =[0,0,0]
            c[0] = a[lna-1]
            c[1] = a[lna]
            c[2] = b[lnb]
            return c
        elif len(a) % 2 != 0 and len(b) % 2 == 0:
            c = [0,0,0]
            c[0] = a[lna]
            c[1] = b[lnb-1]
            c[2] = b[lnb]
            return c
        else:
            print("Please enter the correct format")

al1 = str(input("Please enter the list seperated with comma ',': "))
bl1 = str(input("Please enter the list seperated with comma ',': "))
a1 = al1.split(',')
b1 = bl1.split(',')
#print(a1)
#print(b1)
print(middle_way(a1,b1))
