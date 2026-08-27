# Build a car game that accepts start car, stop car and quit game commands.
'''
    Game Rules:
    Type 'start car' or 'stop car' to start or stop the car
    Type 'quit game' to exit the game
    Type 'help' to view the game rules
    If you enter anyother command you will get an error.
'''

help_message = """
start car - to start the car
stop car - to stop the car and
quit game - to exit the game
no other commands are recognized by this game.
"""
print("<<-- Fun Car Game -->>")
user_input = ""
is_started = False
# is_stopped = 0  # created it to use as a counter based variable. Later switched to boolean check.

# while user_input != "quit game": --> this can also be written as
while True:
    user_input = input("--> ").lower()
    if user_input == "help":
        print(help_message)
    elif user_input == "start car":
        if is_started: # using boolean check
            print("Car is already started. Try another command!")
        else:
            print("Car started... Ready.. Steady.. Gooo!!!")
            is_started = True
    elif user_input == "stop car":
        # if is_stopped == 0: # using a counter variable based check. But it won't work properly because you can stop the car without even starting it.
        #     print("Car stopped. You can now safely offboard the car.")
        #     is_stopped += 1
        # else:
        #     print("Car already stopped. Try 'quit game' command instead.")    
        if not is_started:
            print("Car is at a stop already!")
        else:
            print("Car stopped. You can now safely offboard the car.")
            is_started = False
    elif user_input == "quit game":
        print("Car game stopped")
        break
    else:
        print("Command not recognized. Please try again or type 'help' to view the game rules.")