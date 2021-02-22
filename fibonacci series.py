def fibonnaci(n):
    a=0
    b=1
    print("Fibonacci series of ",n," terms : ")
    print(a)
    print(b)
    for i in range(1,n-1):
        s=a+b
        print(s)
        a=b
        b=s
n=int(input("Enter number of terms : "))
fibonnaci(n)
