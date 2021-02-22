class Bird:
    wings=2
    def _init__(self):
        print("Bird is ready to fly")

    def WhoisThis(self):
        print("bird")

    def Swim(self):
        print("it fly faster")

    
class Penguine(Bird):
        def __init(self):
            super().__init__()
            print("Penguine is ready to swim")

        def WhoisThis(self):
            print("Penguine")
            print("Wings of Penguine are",super().wings)

        def Run(self):
            print("It run faster")
        
B=Bird()
P=Penguine()
P.WhoisThis()
P.Swim()