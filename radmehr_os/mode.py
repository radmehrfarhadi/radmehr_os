developer_mode = False

def mode():
    print("change to developer mode")

    hashed_password = b"$2b$12$xrSfcZ3fgg4AS.joH4cuye6b9qAQpsMeLiCiw1ZsMP8tmjkHjAvpy"

    try:
        import bcrypt

        password2 = input("password: ")
        if bcrypt.checkpw(password2.encode("utf-8"), hashed_password):
            print("Developer mode enabled.")
            return True

        print("Access denied!")
        return False

    except BaseException as error:
        print(f"Developer mode error: {type(error).__name__}: {error}")
        print("Returning to Settings instead of closing the program.")
        return False
