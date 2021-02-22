def perfect(n):
    s=0
    for i in range(1,n):
        if(n%i==0):
            s=s+i
    
    print("Sum :",s)
    if(s==n):
        print("Number",n,"is perfect number")
    else:
        print("Number",n,"is not a perfect number")

n=int(input("Enter the number : "))
perfect(n)