# Area calculation program

print "Welcome to the Area calculation program"
print "---------------------------------------"
print

# Print out the menu:
print "Please select a shape:"
print "1  Rectangle"
print "2  Circle"

# Get the user's choice:
shape = input("> ")

# Calculate the area:
if shape == 1:
    height = input("Please enter the height: ")
    width = input("Please enter the width: ")
    area = height*width
    print "The area is", area
else:
    radius = input("Please enter the radius: ")
##  Note the  ** -> power operator
    area = 3.14*(radius**2)
    print "The area is", area
#Yes there is a else if --- elif
