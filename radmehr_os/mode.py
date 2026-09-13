import bcrypt

developer_mode = False
def mode():
    print("chenge to developer mode")

    with open("radmehr_os/password.txt", "r") as file:
        hashed_password = file.read()
        password2 = input("password: ")
        if bcrypt.checkpw(password2.encode(),hashed_password.encode()):
            return True
        else:
            print("Access denied!")
            return False