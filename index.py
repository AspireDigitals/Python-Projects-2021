# Multiple variable assignment
#first_name, sur_name = "Isaac", "Kwakye"
#print(first_name, sur_name)
#index
Students = {"Kofi" : 28, "Samuel" : 50}
for i in Students:
    print(i)

students = {"Males" : ("samuel", "Kofi", "joe"), "Females" : ("amina", "asi", "ella")}
print(students["Males"][0])


schools = ("swesco", "adisco", "botwey")
name = input("name: ")
if name in Students:
    if name == 28:
        print(name, "you were placed at", schools[0])

FirstName, SurName, OtherName, Location, Read, FollowedBy = "Isaac", "Kwakye", "Quashie", "Wassa Akropong", "I am called", "I am from"                                                             
print(Read, FirstName[0], SurName[4], OtherName[3],)
print(FollowedBy, Location)


#Logical or arithmetic operations
# + addition, - subtraction, / division, * multiplication, % modulo/remainder, == equal to, === identical, != not equal to, !== not identical, > greater than, < less than, powers **
print(3 + 5)
print(7 / 6)
print(6 % 5)
print(3 * 4)
print(5 > 4)
print(5 != 4)

#data structures
# List
# Dictionary

Students = ("Amina seidu", "Lizzy arthur", "Isaac kwakye", "Alex mensah")
print(Students[0])
print(Students[2][8])


#Dictionary

Students = {1 : "isaac", 2 : "Course Guide", 3 : "Lizzy"}
print(Students [2])

Schools = {340 : "Swesco", 456 : "Adisco", 676 : "Mfantsiman"}
print(Schools [456])



# If, Elif (Else if), Else statement

a, b = 35, 7
if a > b:
    print("Yes")
else:
    print("No")

x = 6
y = 8
z = x + y
if z - x == y:
    print(z - x, "is equal to", y)
else:
    print(z - x, "is not equal to", y)

a, b = 9, 9
if a > b:
    print("true")
elif a < b:
    print("false")
elif a == b:
    print("okay")
elif a != b:
    print("No")
else:
    print("I am okay")




#Input
#a = input("Enter first number ")
#b = input("Enter second number ")
#c = a + b
#print(c)


#name = input("Enter name here: ")
#color = input("Enter favourite color here: ")
#print(name, "likes", color)


#x = input()
#y = input()
#z = x + y
#print(z)

#int 
#str

#name = input("Enter your name here: ")
#first_number = int(input("Enter your first number here: "))
#second_number = int(input("Enter second number here: "))
#print(name, "the sum of your numbers is", first_number + second_number)


name = input("Enter your name here: ")
year_of_birth = int(input("Enter your yearof birth here: "))
current_year = int(input("Enter current year here: "))
age = current_year - year_of_birth
if age < 18:
    print(name, "You are", age, "years old and don't qualify")
else:
    print(name, "You are", age, "years old and qualifies")


