try:
    rows = int(input("Enter the  number of rows :"))
    if(rows>0):
        m = (2 * rows) - 2
        for i in range(1, rows+1):
            for j in range(1, m):
                print(end=" ")
            m = m - 1
            for j in range(i, 0, -1):
                print(j, end=' ')
            print(" ")
    else:
        print("Number of rows is invalid")
except ValueError:
    print("Enter a natural number")
