# Simple inputs and variables
full_name = input("Enter patient's full name: ")
age = input("Enter patient's age: ")
is_new_patient = input("Is the patient new? (provide True or False): ")

# Print collected patient details
print(full_name + " age " + age + ", is a patient")

# While Loop
iterator = int(input("Enter iterator value: "))
while iterator <= 7:
    print('<>' * iterator)
    iterator += 1
print("While loop is completed")


# Write code for a guessing game. Fetch the guess number from user, compare it with the predefined/actual number.
# If the user guessed the number correctly, print "Congrats! You've guessed the number correctly".
# If the user guessed the number incorrectly, print "Sorry! You've guessed the number incorrectly. Please try again".
# Give the user 3 chances to guess the number

number = 6
print("*****GUESSING GAME*****")
print("You have 3 chances to guess the number. Guess a number between 0 & 10")

for i in range(3):
    user_guess = int(input("Input your guess: "))
    if user_guess == number:
        print("Congrats! You've guessed the number correctly")
        break
    else:
        print("Sorry! You guessed the wrong number. Please try again")
        print("You have " + str(2 - i) + " chances left")

print("You've exhausted all 3 chances. Better luck next time!")


# Write down the same guessing game using while loop

secret_number = 8
chance_count = 1
chance_limit = 3
while chance_count <= chance_limit:
    guess_number = int(input("Enter your guess: "))
    if guess_number == secret_number:
        print("You won!")
        break
    chance_count += 1
else:
    print("Sorry, You lose!")


