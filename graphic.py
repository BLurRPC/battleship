def showTable (myTable):
    for i in range(10):
        print(str(9 - i) + " ", sep = ' ', end ='')
        for j in range(10):
            print(myTable[9 - i][j] + " ", sep=' ', end='')
            if j==9:
                print("\n")
    for k in range(10):
        print("  " + str(k), sep = ' ', end ='')
    print("\n")