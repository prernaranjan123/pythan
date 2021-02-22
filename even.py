s=int(input("Enter number for checking odd/even"))
def even(s):
    if(s%2==0):
        print("Number is even")
    else:
        print("Number is odd")
even(s)

print("USing filter")
def even(s):
    return s%2==0
def odd(s):
    return s%2==1
l=[34,5,34,67,756,4,4,5,7,987,1]
x=list(filter(even,l))
y=list(filter(odd,l))
print("List of even numbers in list",x)
print("List of even numbers in list",y)
print("zip value of list",tuple(zip(x,y)))
