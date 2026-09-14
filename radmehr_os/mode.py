from pathlib import Path
import hashlib
import hmac
import sys

developer_mode = False

def _password_file():
    if getattr(sys, "frozen", False):
        base = Path(sys.executable).resolve().parent
        if sys.platform == "darwin":
            return base / "data" / "password.hash"
        return base / "radmehr_os" / "password.hash"
    return Path(__file__).resolve().parent / "password.hash"

def mode():
    print("change to developer mode")

    try:
        hash_path = _password_file()
        stored_hash = hash_path.read_text(encoding="utf-8").strip()

        password = input("password: ")
        entered_hash = hashlib.sha256(password.encode("utf-8")).hexdigest()

        if hmac.compare_digest(entered_hash, stored_hash):
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
