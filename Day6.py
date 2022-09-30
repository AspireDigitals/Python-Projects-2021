#Calculator
#AREA CALCULATOR
#AREA OF A SQUARE = LENGHT * HEIGHT OF THE SQUARE
#QUESTION

first_number = int(input("Enter first number here: "))
second_number = int(input("Enter second number here: "))
operator = input("Choose mathematical operator: ")

# +, -, *, /, **, %
if operator == "+":
    print("The sum of the sumbers is", first_number + second_number)
elif operator == "-":
    print("The difference of the numbers is", first_number - second_number)

#AGE CALCULATOR

requirement = (18)
name = input("Enter name here: ")
year_of_birth = int(input("Enter year of birth: "))
current_year = int(input("Enter current year: "))

age = current_year - year_of_birth
print(age)

if age < requirement or age > 60:
    print(name, "You do not meet the requirement")
else:
    print(name, "you have been accepted")



account_balance = 0
transaction_amount = int(input("Enter amount: "))
transaction_type = input("Enter transaction type: ")

if transaction_type == "1":
    account_balance += transaction_amount
    print("Your new account balance is", account_balance)
elif transaction_type == "2":
    account_balance -= transaction_amount
    if account_balance <= transaction_amount:
        print("Transaction not allowed")
        print(account_balance)
    else:
        print("Your new account balance is", account_balance - transaction_amount)


amount = int(input("Enter amount in cedis: "))
converter = input("Choose converter: ")

if converter == "$":
    print(amount, "Cedis is equal to", amount / 6.18, "in dollars")
elif converter == "!":
    print(amount, "Cedis is equal to", amount / 8.35, "in pounds")


a = 5
print(a / 100, "%")


character = ("round face", "big but", "fair", "tall")
question1 = input("What is the shape of your face ? ")
question2 = input("What is the size of your but ? ")
question3 = input("What is your height ? ")

if question1 in character or question2 in character or question3:
    print("You have a match")
else:
    print("you don't have a match")
