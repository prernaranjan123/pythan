def magic(n):
    s=n
    sum=0
    while(s>9):
        while(s>0):
            d=s%10
            sum=sum+d
            print(sum)
            s=s//10

        s=sum
    

    if(s==n):
        print("Number",n,"is magic number")
    else:
        print("Number",n,"is not a magic number")

n=int(input("Enter the number : "))
magic(n)