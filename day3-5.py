M = int(input("Enter the starting number of range: "))

N = int(input("Enter the ending number of range: "))
if(N>M)and(M>0):
    K = int(input("Enter the numbers to be skipped in range: "))
    if(K>0):
        for i in range(M, N + 1, K+1):
            print(i)
    else:
        print("K value cannot be negative")

else:
    print("Enter valid input")
