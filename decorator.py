
def add_ten(number):
    def add_one(number):
       return number+1
    result=add_one(number)
    return result+10
print(add_ten(10))




