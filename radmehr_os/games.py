import random

def Games():
    while True:
        print("1. Number Guessing")
        print("2. Rock Paper Scissors")
        print("3. exit")
        inputs = int(input("enter number! "))
        if inputs == 1:
            gessing_number = random.randint(1, 100)
            guess_num = 0
            while True:
                gessed = int(input("you are gessed... "))
                if gessed > gessing_number:
                    print("Too high!")
                    guess_num+=1
                    continue
                if gessed < gessing_number:
                    print("Too low!")
                    guess_num+=1
                    continue
                if gessed == gessing_number:
                    guess_num+=1
                    print(f"You won in {guess_num} guesses! 🎉🚀")
                    break
        if inputs == 2:
            com = ["rock","paper","scissors"]
            while True:
                com_com = random.choice(com)
                player = input("rock or paper or scissors??? ")
                if player not in com:
                    print("Invalid choice!")
                    continue
                print(f"Computer chose: {com_com}")
                if player == "rock" and com_com == "scissors":
                    print("You won!")
                    break
                elif player == "paper" and com_com == "rock":
                    print("You won!")
                    break
                elif player == "scissors" and com_com == "paper":
                    print("You won!")
                    break
                elif player == com_com:
                    print("Draw!")
                    continue
                else:
                    print("computer won!")
                    break
        if inputs == 3:
            print("choose your fild:")
            print("1. Games")
            print("2. AI")
            print("3. Space")
            print("4. Tools")
            print("5. Settings")
            print("0. Exit")
            return
        
