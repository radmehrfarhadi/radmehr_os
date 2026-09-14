from pathlib import Path
import base64
import hashlib
import hmac
import sys

developer_mode = False

def _password_file():
    if getattr(sys, "frozen", False):
        return Path(sys.executable).resolve().parent / "radmehr_os" / "password.hash"
    return Path(__file__).resolve().parent / "password.hash"

def _check_password(password, stored):
    try:
        algorithm, iterations, salt_b64, digest_b64 = stored.split("$", 3)
        if algorithm != "pbkdf2_sha256":
            return False

        salt = base64.b64decode(salt_b64)
        expected = base64.b64decode(digest_b64)
        actual = hashlib.pbkdf2_hmac(
            "sha256",
            password.encode("utf-8"),
            salt,
            int(iterations),
        )
        return hmac.compare_digest(actual, expected)
    except (ValueError, TypeError):
        return False

def mode():
    print("change to developer mode")

    try:
        hash_path = _password_file()
        stored = hash_path.read_text(encoding="utf-8").strip()
        password = input("password: ")

        if _check_password(password, stored):
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
