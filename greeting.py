name = input("Enter your name here")
time = int(input("Whats the time now ? "))
if time < 12:
    print("Good Morning", name)
elif time > 12 and  < 16:
    print("Good Afternoon", name)
elif time > 16 and < 12:
    print("Good Evening", name)