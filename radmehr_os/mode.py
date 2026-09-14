import bcrypt

developer_mode = False

def mode():
    print("change to developer mode")

    hashed_password = b"$2b$12$xrSfcZ3fgg4AS.joH4cuye6b9qAQpsMeLiCiw1ZsMP8tmjkHjAvpy"

    try:
        password2 = input("password: ")
        if bcrypt.checkpw(password2.encode("utf-8"), hashed_password):
            print("Developer mode enabled.")
            return True
        else:
            print("Access denied!")
            return False
    except (ValueError, TypeError) as error:
        print(f"Could not check developer password: {error}")
        return False
