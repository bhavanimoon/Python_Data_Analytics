# Exploring try, except

try:
    age = int(input(">> Enter user's age:  "))
    income = int(input(">> Enter income:  "))
    risk = income / age
    print(f"User's income risk is {risk}")
except ZeroDivisionError:
    print("Age cannot be Zero(0)")
except ValueError:
    print("Only integers accepted. No string or characters")
