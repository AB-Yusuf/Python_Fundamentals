#starting Time - 9.40am
#Paused - 12:00pm
#Input is a base 10 integer n
#convert it to base2
#Print the number of CONsecutive 1's in n representation


#To convert from base 10 to base 2


# def consecutiveNumberChecker(number):
    
#     listValues = []
#     #Converting it to base 2
#     while number != 0:
        
#         remainder = number%2
#         listValues.append(remainder)
#         number = number//2
    
#     listValues.reverse()
#     #newList = [str(i)for i in listValues]
    
#     # newList = []
#     # for i in listValues:
#     #   newList.append(str(i))
#     # counter = 0  
#     # length = len(listValues)
    
#     return listValues


# def looper(loopListValues):
#     loopcounter = 0
#     for i in loopListValues:
#         if i == 1:
#             loopcounter+=1
          
#     return loopcounter    
    
    
    

# #Where the number here is 1
# # def consecutiveNumberChecker(number):
# #     counter = 0
# #     for i in number:
# #         if i == 1:
# #             counter+=1
# #         else:
# #             print(counter)
# #             break

# if __name__ == '__main__':
    
#     userInput = int(input())
#     changingCounter = 0
#     realCounter = 0

#     listValues = consecutiveNumberChecker(userInput)
#     while listValues:
#         changingCounter = looper(listValues)
        
#         if changingCounter <= realCounter:
#             realCounter = realCounter
#         else:
#             realCounter = changingCounter 

#         if len(listValues) != 1:
#             listValues = listValues[changingCounter+1:]
#         else:
#             print(realCounter)
#             break
            


def consecutiveNumberChecker(number):
    listValues = []

    while number!= 0:
        remainder = number%2
        listValues.append(remainder)
        number = number//2

    listValues.reverse()
    
    return listValues

def looper(loopListValues):
    loopcounter = 0
    zeroCounter = 0

    for i in loopListValues:
        if i == 1:
            loopcounter+=1
        else:
            break
        
    return loopcounter



if __name__ == '__main__':

    n = int(input())
    changingCounter = 0
    realCounter = 0
    alistValues = []

    alistValues = consecutiveNumberChecker(n)
    while alistValues:
        changingCounter = looper(alistValues)

        if changingCounter <= realCounter:
            realCounter = realCounter
        else:
            realCounter = changingCounter

        if alistValues[0] != 0:
            alistValues = alistValues[changingCounter-1:]
        else:
            alistValues = alistValues[len(alistValues)-len(alistValues):]
        
        if len(alistValues) != 1:
            alistValues = alistValues[len(alistValues)-(len(alistValues)-1):]
        else:
            print(realCounter)
            break
    
















































    
    
    
    

    
    