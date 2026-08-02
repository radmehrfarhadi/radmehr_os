import subprocess

def backup():
    result = subprocess.run(
        ["git", "status", "--porcelain"],
        capture_output=True,
        text=True
    )

    if result.stdout.strip() == "":
        print("No changes. Backup skipped.")
        return

    result1 = subprocess.run(["git", "add", "."])

    if result1.returncode == 0:
        print("Successfully added files to git.")
    else:
        print("Failed to add files to git.")
        return

    result2 = subprocess.run(
        ["git", "commit", "-m", "Radmehr OS backup"]
    )

    if result2.returncode == 0:
        print("Successfully committed changes.")
    else:
        print("Failed to commit changes.")
        return
    result3 = subprocess.run(["git", "pull", "--rebase"])

    if result3.returncode == 0:
        print("git rebase is Successfully .")
        #🚀
    else:
        print("Failed git rebase")
        return

    result4 = subprocess.run(["git", "push"])
    if result4.returncode == 0:
        print("Git push completed successfully.")
        print("Backup completed 🚀.")
    else:
        print("Failed to push changes.")
        return
