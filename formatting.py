class student:
    course="python"
    def __init__(self,rn,name):
        self.Roll_No=rn
        self.Name=name
    def info(self):
        print("Roll no : {} and Name : {}".format(self.Roll_No,self.Name))
obj=student(1,"Abhishek")
obj.info()
obj1=student(2,"Kirti")
print("Course : ",obj1.__class__.course)
obj1.__class__.course="php"
obj1.info()
print("Course : ",obj1.__class__.course)