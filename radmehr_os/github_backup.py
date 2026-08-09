import subprocess
from radmehr_os.backup_history import get_backup_time

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
        print(result1.stderr)
        return
    commit = input("whats your commit?")
    if commit == "":
        commit = "Radmehr OS backup"
    result2 = subprocess.run(
        ["git", "commit", "-m", f"{commit}"]
    )

    if result2.returncode == 0:
        print("Successfully committed changes.")
    else:
        print("Failed to commit changes.")
        print(result2.stderr)
        return
    result3 = subprocess.run(["git", "pull", "--rebase"])

    if result3.returncode == 0:
        print("Git rebase completed successfully.")
    else:
        print("Failed git rebase")
        print(result3.stderr)
        return

    result4 = subprocess.run(["git", "push"])
    if result4.returncode == 0:
        backup_time = get_backup_time()
        print("Git push completed successfully.")
        print(f"Backup completed 🚀 at {backup_time}")
        
    else:
        print("Failed to push changes.")
        print(result4.stderr)
        return
