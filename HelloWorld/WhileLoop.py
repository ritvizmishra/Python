# Print Pattern
i = 1
while i <= 5:
    print('*' * i)
    i = i + 1
print("Done")

# Guess game
secret_num = 9
i = 1
while i <= 3:
    guess = input("Guess: ")
    if int(guess) == secret_num:
        print("Good job!")
        break
    i += 1
else:
    print("Sorry, you failed.")

# Car Game
command = ""
flag = False

while True:
    command = input("> ").lower()
    if command == "start":
        if flag:
            print("Car is already running")
        else:
            flag = True
            print("Car Started...")
    elif command == "stop":
        if not flag:
            print("Car is already stopped.")
        else:
            flag = False
            print("Car Stopped.")
    elif command == "help":
        print('''
> start - to start the car
> stop - to stop the car
> quit - to end the game''')
    elif command == "quit":
        print("Game Over!")
        break
    else:
        print("I don't understand this.")





