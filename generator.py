def arthimatic_generator(n):
    print("Inside my generator")
    if(n%2==0):
     yield("even")
    else:
     yield("odd")
for value in arthimatic_generator(45):
    
