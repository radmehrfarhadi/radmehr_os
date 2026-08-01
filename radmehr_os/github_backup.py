import subprocess

def backup():
    result1 = subprocess.run(["git", "add", "."])
    if result1.returncode == 0:
        print("successfully added files to git.")
    if result1.returncode != 0:
        print("failed to add files to git.")
        return
    result2 = subprocess.run(["git", "commit", "-m", "Radmehr OS backup"])
    if result2.returncode == 0:
        print("successfully committed changes.")
    elif result2.returncode != 0:
        print("failed to commit changes.")
        return
    result3 = subprocess.run(["git", "push"])
    if result3.returncode == 0:
        print("Backup completed 🚀.")
    else:
        print("failed to push changes.")
        return