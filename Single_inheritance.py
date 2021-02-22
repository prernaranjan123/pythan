class a:
    def show(self):
        print("hello Iphone 12")
obj=a()
obj.show()

class b:
    def show(self):
        print("Pro max")
obj1=b()
obj1.show()


print("importing function of demo class")
from demo_lib import demo
print ("this is demo function from demo class")
d=demo()
d.fun_demo()