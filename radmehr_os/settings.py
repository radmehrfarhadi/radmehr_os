def Settings():
    try:
        with open("name_radmehr_os.txt", "r") as file:
            name = file.read()
    except FileNotFoundError:
        name = ""

    print(f"name = {name}. for edit plase wreat (plase) but if dont you can say (enter)")
    plase = input("")

    if plase == "plase":
        new_name = input("whats your new name? ")

        with open("name_radmehr_os.txt", "w") as file:
            file.write(new_name)

    print("for chat with ai plase enter your api. for wreat plase wreat (plase) but if dont you can say (enter)")

    ai = input("")

    if ai == "plase":
        api_key = input("whats your api_key? ")

        with open("api_key_radmehr_os.txt", "w") as file:
            file.write(api_key)