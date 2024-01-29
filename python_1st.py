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
# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str
    
# your code goes here
# We should define car1 and car2 as part of the vehicle class, otherwise any values assigned
# will be undefined.
# object variables
car1 = Vehicle()
car2 = Vehicle()

# Using the parameters of the vehicle class and what the exercise entails, we can infer
# that name, kind, and color are strings, so those will be given values with double quotations;
# on the other hand, value appears to have a float as a value, so a numerical value will
# be given with two decimal places.
# car1 information
car1.name = "Fer"
car1.kind = "convertible"
car1.color = "red"
car1.value = 60000.00

#car2 information
car2.name = "Jump"
car2.kind = "van"
car2.color = "blue"
car2.value = 10000.00

# test code
# The test code prints out all the information about car1 and car2.
print(car1.description()) # Prints out car1's description.
print(car2.description()) # Prints out car2's description.

print("check check")
print("This is charles.")
print("Double checking for Sprint mobile.")
