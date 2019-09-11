#Create a phonebook 
#The number of entries to be made into the phonebook == n
#Each Entry is stored in the phonebook
#Entry will be 2 spaced separated values
#first value is the Key
#second value is the value
#After the number of n entries have been made
#The phonebook will be queried
#Unknown number of queries
#Keep accepting query until there is no more input, program should end
#If query is found Output is in this format "name=phoneNumber"
#query is in small letters
#if query is not found Output = "Not Found"


# released = {
    
#     "iphone":2007,
#     "iphone 3G":2008,
#     "inphone 4":2009
# }



# for item in released:
#     count[item] = count.get(item, 0) + 1
#     print(count[item])


phoneDictionary = {}
numberOfEntries = int(input())

counter = 0

#This will be in a while loop
while counter < numberOfEntries:
    userText = input()
    key, value = userText.split()
    phoneDictionary[key] = value
    counter+=1

print(phoneDictionary)


#To perform query
query = input()

while query:
    try:
        if query in phoneDictionary:
            print(query+"="+phoneDictionary[query])
        else:
            print("Not found")
    
        query = input()
        
    except(EOFError):
        break