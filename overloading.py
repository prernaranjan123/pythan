class sum:
    def add(self,fn,sn):
        fn=int(input("this is first number"))
        sn=int(input('this is second number'))
        return(fn+sn)
    def add(self,fn,sn,tn=0):
        return(fn+sn+tn)
obj=sum()
sum1=obj.add(10,20,90)
print("Sum",sum1)