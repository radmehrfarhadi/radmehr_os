from github_backup import backup
import bcrypt

def Settings():
    try:
        with open("name_radmehr_os.txt", "r") as file:
            name = file.read()
    except FileNotFoundError:
        name = ""

    while True:
        print("1. edit gemini api")
        print("2. edit nasa api")
        print("3. edit your name")
        print("4. backup github")
        print("5. show last backup time")
        print("6. exit")
        choose = int(input("choose!! choose!!!!"))
        if choose == 1:
            gemini_api = input("whats your new gemini api? ")
            with open("api_key_radmehr_os.txt","w") as file:
                file.write(gemini_api)
        elif choose == 2:
            nasa_api = input("whats your new nasa api? ")
            with open("nasa_api_key.txt","w") as file:
                file.write(nasa_api)
        elif choose == 3:
            name = input("whats your new name? ")
            with open("name_radmehr_os.txt","w") as file:
                file.write(name)
        elif choose == 4:
            with open("radmehr_os/backup_password.txt","r") as file:
                hashed_password = file.read()
            password2 = input("password: ")
            if bcrypt.checkpw(password2.encode(),hashed_password.encode()):
                backup()
            else:
                print("you are denger e denger!!!")

            
        elif choose == 5:
            try:
                with open("last_backup.txt", "r") as file:
                    time = file.read()
                print("Last backup:")
                print(time)
            except FileNotFoundError:
                print("No backup found yet.")
        elif choose == 6:
            return