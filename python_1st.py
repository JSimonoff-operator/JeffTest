# the dictionary phonebook, defined with John, Jack, and Jill with their phone numbers
phonebook = {  
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}  
# your code goes here
# To add Jake into the phonebook, all we need to do is bring up the dictionary's name,
# write Jake into the index, and define said addition with his phone number.
phonebook["Jake"] = 938273443

# In order to delete Jill from the phonebook, we merely need to use del with the defined
# definition and element.
del phonebook["Jill"]
# testing code
# This if statement checks for the string "Jake" in the phonebook. If he's there,
# the statement below will print itself out.
if "Jake" in phonebook:  
    print("Jake is listed in the phonebook.")

# This if statement checks for the string "Jill" in the phonebook. If she isn't there,
# the statement below will print itself out.
if "Jill" not in phonebook:      
    print("Jill is not listed in the phonebook.") 

