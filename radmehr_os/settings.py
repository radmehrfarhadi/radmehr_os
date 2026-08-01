from github_backup import backup

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
            backup()
        elif choose == 5:
            return