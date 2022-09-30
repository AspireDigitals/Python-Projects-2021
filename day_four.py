from math import *
import math
numbers = 2, 4, 6, 7, 9
print(max(numbers))


print(math.floor(5.6))
 
 #ceil
 #floor
 #max
 #min
# Loops

# for loop

for i in range(5):
    print(i + 1)


x = ("kofi", "ama", "badu", "samuel")
for i in x:
    print(i)


students = {"males" : ("kofi", "samuel", "isaac"), "females" : ("asi", "abigail", "martha")}
for i in students:
    print(students["males"], students["females"])


for i in range(10):
    print("i love coding")


#while

x = 4
while True:
    for i in range(5):
        print(i, "i love you")

x = 2
y = 5
while x < y:
    for i in range(50):
        x += 1
        print(x)


#external modules

