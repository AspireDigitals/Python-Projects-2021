#Multiple assignment or declaration of variables
#Logical or mathematical/arithmetic operations
#Data structures
#Lists
#Dictionary

age1 = 6
age2 = 5
age3 = age1 % age2
print(age3)









students = ("abby", "joe", 4)
for i in students:
    print("i love", i)









name = input("Enter your name here: ")
malariaSymptoms = ("fever", "headache")
symptoms = input("Enter your symptom here: ")
for i in malariaSymptoms:
    if symptoms in malariaSymptoms:
        print(name, "you have malaria")
    else:
        print(name, "you don't have malaria")










name = input("Enter your name here: ")
malariaSymptoms = ("fever", "headache")
symptoms = input("Enter your symptom here: ")
for i in malariaSymptoms:
    if symptoms in malariaSymptoms:
        print(name, "you have malaria")
    else:
        print(name, "your sickness was not found")