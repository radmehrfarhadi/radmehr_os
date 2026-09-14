import sys
import traceback
from space import Space
from ai import AI
from games import Games
from settings import Settings
from tools import Tools

sys.stdout.reconfigure(encoding="utf-8")
sys.stdin.reconfigure(encoding="utf-8")

def main():
    hello()
    get_name_and_print()
    menu()

def hello():
    with open("radmehr_os/version.txt", "r") as file:
        version = file.read()

    print(f"hello welcome to the radmehr_os v{version}!")

def get_name_and_print():
    try:
        with open("name_radmehr_os.txt", "r") as file:
            name = file.read()
    except FileNotFoundError:
        name = ""

    if name == "":
        name = input("whats your name?")
        with open("name_radmehr_os.txt", "w") as file:
            file.write(name)
        print(f"oh {name}! welcome!")
    else:
        print(f"oh {name}! welcome!")

def Exit():
    sys.exit()

def menu():
    print("choose your field:")
    print("1. Games")
    print("2. AI")
    print("3. Space")
    print("4. Tools")
    print("5. Settings")
    print("0. Exit")

    while True:
        while True:
            try:
                ne = int(input("Please enter your number: "))
                break
            except ValueError:
                print("Please enter a number!")

        valid_choices = [0, 1, 2, 3, 4, 5]

        if ne == 1:
            Games()
        elif ne == 2:
            AI()
        elif ne == 3:
            Space()
        elif ne == 4:
            Tools()
        elif ne == 0:
            Exit()
        elif ne == 5:
            Settings()
        elif ne not in valid_choices:
            print("Invalid choice!")

if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        raise
    except BaseException:
        print("\n=== RADMEHR OS ERROR REPORT ===")
        traceback.print_exc()
        print("\nThe program hit an error, but CMD will stay open.")
        try:
            input("\nPress Enter to close...")
        except BaseException:
            pass
