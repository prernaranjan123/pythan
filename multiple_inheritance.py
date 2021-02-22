class program:
    
    def show(self,name,std):
        print("Name:",name)
        print("Class",std)
obj=program()
obj.show('abhi',10)

class subject():
    def show_marks(self,sub):
        print("Maths",sub)
obj1=subject()
obj1.show_marks(10)

class r_no(program,subject):
    def show_roll(self,r_no):
        print("Roll",r_no)
obj2=r_no()
obj2.show('abhi',12)
obj2.show_marks(10)
obj2.show_roll(23)





