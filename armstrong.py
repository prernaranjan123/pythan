def armstrong(n):
    i=n
    s=0
    while(i!=0):
        d=i%10
        s=s+d*d*d
        i= i//10
    print("Sum : ",s)
    if(s==n):
         print("Number",n,"is Armstrong number")
    else:
        print("Number",n,"is not an Armstrong number")
n=int(input("Enter number to check armstrong : "))
armstrong(n)