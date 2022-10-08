a=int(input("Enter the number of words: "))
words=[]
if(a>0):
    for i in range (0,a):
        c=input("Enter the word: ")
        words.append(c)
    print("The List of words : ",words)
    choice=input("Enter thechoice A/D: ")
    if(choice=='A'):
        words.sort()
        print('List in Ascending Order: ', words)
    else:
        words.sort(reverse=True)
        print('List in Descending Order: ', words)
else:
    print("Enter valid input")
