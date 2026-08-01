import random

def Games():
    tas = [1, 2, 3, 4, 5, 6]
    while True:
        print("1. Ludo")
        print("2. exit")
        inputs = int(input("enter nember! "))
        if inputs == 1:
            tas_ = random.choice(tas)
        if inputs == 2:
            print("choose your fild:")
            print("1. Games")
            print("2. AI")
            print("3. Space")
            print("4. Tools")
            print("0. Exit")
            return
        print(f"tas is {tas_}")
