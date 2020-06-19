def cellChange(cell,days):
    newarr = cell[:]
    n  = len(cell)
    for k in range(days):
        for i in range(0,len(cell)):
            cell[i] = int(cell[i])
        if cell[1] == 0:
            newarr[0] = 0
        else:
            newarr[0] = 1

        if cell[-2] == 0:
            newarr[-1] = 0
        else:
            newarr[-1] = 1
        for j in range(1,n-1):
            if cell[j-1] - cell[j+1] == 0:
                newarr[j] = 0
            else:
                newarr[j] = 1

        print('Day {} infected are {}'.format(k+1,newarr))
        print('--------------------------------------------------------')
        cell = newarr[:]
    return newarr


cell_entry = input("Enter the list with 8 bit in 1's and 0's with comma as seperated : ")
ls1 =cell_entry.split(',')
#print(ls1)
days = int(input("Enter the days: "))
print(cellChange(ls1,days))
