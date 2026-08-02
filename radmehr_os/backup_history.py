from datetime import datetime
def get_backup_time():
    now = datetime.now()
    time = now.strftime("%Y-%m-%d %H:%M:%S")
    with open("last_backup.txt","w") as file:
        file.write(time)
    return time