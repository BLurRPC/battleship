def showTable (myTable):
    for i in range(10):
        for j in range(10):
            print(myTable[i][j], sep='  ', end='')
            if j==9:
                print("\n")
