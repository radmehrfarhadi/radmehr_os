import bcrypt

developer_mode = False
def mode():
    print("chenge to developer mode")

    hashed_password = "$2b$12$xrSfcZ3fgg4AS.joH4cuye6b9qAQpsMeLiCiw1ZsMP8tmjkHjAvpy"
    password2 = input("password: ")
    if bcrypt.checkpw(password2.encode(),hashed_password.encode()):
        return True
    else:
        print("Access denied!")
        return False