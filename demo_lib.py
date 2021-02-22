class demo:
    def demo(self):
        print("this is default constructor")
    def __init__(self):
        print("this is parametrized constructor")
    def fun_demo(self):
        print("this is fun_demo function")   
obj=demo()
obj.fun_demo()