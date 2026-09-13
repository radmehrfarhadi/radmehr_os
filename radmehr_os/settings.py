from github_backup import backup
from mode import mode

def Settings():
    developer_mode = False
    try:
        with open("name_radmehr_os.txt", "r") as file:
            name = file.read()
    except FileNotFoundError:
        name = ""
    while True:
        if developer_mode == True:
            print("1. edit gemini api")
            print("2. edit nasa api")
            print("3. edit your name")
            print("4. backup github")
            print("5. show last backup time")
            print("6. edit version")
            print("7. exit")
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
                backup()

            
            elif choose == 5:
                try:
                    with open("last_backup.txt", "r") as file:
                        time = file.read()
                    print("Last backup:")
                    print(time)
                except FileNotFoundError:
                    print("No backup found yet.")
            elif choose == 6:
                new_version = input("whats new version?")
                with open("radmehr_os/version.txt", "w") as file:
                    file.write(new_version)
            elif choose == 7:
                return
        elif developer_mode == False:
            print("1. edit gemini api")
            print("2. edit nasa api")
            print("3. edit your name")
            print("4. enter developer mode")
            print("5. exit")
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
                developer_mode = mode()
            elif choose == 5:
                return