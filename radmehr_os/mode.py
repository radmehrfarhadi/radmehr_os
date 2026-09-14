from pathlib import Path
import sys

developer_mode = False

def _password_file():
    if getattr(sys, "frozen", False):
        return Path(sys.executable).resolve().parent / "radmehr_os" / "password.hash"
    return Path(__file__).resolve().parent / "password.hash"

def mode():
    print("change to developer mode")

    try:
        import bcrypt

        hash_path = _password_file()
        hashed_password = hash_path.read_bytes().strip()

        password2 = input("password: ")

        if bcrypt.checkpw(password2.encode("utf-8"), hashed_password):
            print("Developer mode enabled.")
            return True

        print("Access denied!")
        return False

    except FileNotFoundError:
        print("Developer password file was not found.")
        print("Returning to Settings instead of closing the program.")
        return False
    except BaseException as error:
        print(f"Developer mode error: {type(error).__name__}: {error}")
        print("Returning to Settings instead of closing the program.")
        return False
