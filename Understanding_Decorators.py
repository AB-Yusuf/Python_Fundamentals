#Understanding decorators
#The whole Purpose is to add new functionality to an existing
#function
#decorators help us extend the functionalities of a function
#without actually modifying the function in concern itself

def check(func):
    def inside(a, b):
        if b == 0:
            print("Can't divide by 0")
            return
        func(a,b)
    return inside

#The decorator below is same thing as
# div = check(div)

@check
def div(a, b):
    return a / b

print(div(10, 0))




    
            
        
        
        
    
