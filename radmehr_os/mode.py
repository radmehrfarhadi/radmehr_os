from pathlib import Path
import base64
import hashlib
import hmac
import os
import secrets
import sys

developer_mode = False

_ITERATIONS = 200_000

def _password_file():
    if getattr(sys, "frozen", False):
        return Path(sys.executable).resolve().parent / "radmehr_os" / "password.hash"
    return Path(__file__).resolve().parent / "password.hash"

def _hide_file(path):
    if os.name == "nt":
        try:
            os.system(f'attrib +h "{path}"')
        except Exception:
            pass

def _make_hash(password):
    salt = secrets.token_bytes(16)
    digest = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        salt,
        _ITERATIONS,
    )
    parts = [
        "pbkdf2_sha256",
        str(_ITERATIONS),
        base64.b64encode(salt).decode("ascii"),
        base64.b64encode(digest).decode("ascii"),
    ]
    return "$".join(parts)

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

def _create_new_password(hash_path):
    print("Developer password needs to be created once.")

    password1 = input("Create developer password: ")
    password2 = input("Repeat developer password: ")

    if not password1:
        print("Password cannot be empty.")
        return False

    if password1 != password2:
        print("Passwords do not match.")
        return False

    hash_path.parent.mkdir(parents=True, exist_ok=True)
    hash_path.write_text(_make_hash(password1), encoding="utf-8")
    _hide_file(hash_path)

    print("Developer password created.")
    print("Developer mode enabled.")
    return True

def mode():
    print("change to developer mode")

    try:
        hash_path = _password_file()

        if not hash_path.exists():
            return _create_new_password(hash_path)

        stored = hash_path.read_text(encoding="utf-8").strip()

        if stored.startswith("$2"):
            return _create_new_password(hash_path)

        password = input("password: ")

        if _check_password(password, stored):
            print("Developer mode enabled.")
            return True

        print("Access denied!")
        return False

    except BaseException as error:
        print(f"Developer mode error: {type(error).__name__}: {error}")
        print("Returning to Settings instead of closing the program.")
        return False
