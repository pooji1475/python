try:
    n=int(input("Enter number:"))
    pal=n
    rev=0
    while(n>0):
        a=n%10
        rev=rev*10+a
        n=n//10
    if(pal==rev):
        print("The number is a palindrome.")
    else:
        print("The number is not a palindrome.")
except ValueError:
    print("Enter only integers")
