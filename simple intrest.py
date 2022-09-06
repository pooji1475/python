def si(principle_amt,roi,time):
    si=(principle_amt*time*roi)/100
    return si
roi=int(input("enter the rate of interest"))
time=int(input("enter the time taken"))
principle_amt=int(input("enter the principle amount"))
simpleinterest=si(principle_amt,roi,time)
print(simpleinterest)
