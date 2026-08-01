from google import genai

def AI():
    try:
        with open("api_key_radmehr_os.txt", "r") as file:
            api = file.read()

    except FileNotFoundError:
        api = ""

    if api == "":
        api = input("whats your api? ")

        with open("api_key_radmehr_os.txt", "w") as file:
            file.write(api)

    print("1. chat with ai")
    print("2. exit")

    entered = int(input("choose choose!! "))

    if entered == 1:
        client = genai.Client(
            api_key=api
        )

        while True:
            message = input("You: ")

            if message == "خداحافظ" or message == "بای" or message == "goodbye" or message == "bye":
                print("Gemini: خداحافظ! 👋")
                break

            response = client.models.generate_content(
                model="gemini-3.5-flash",
                contents=message
            )

            print("Gemini:", response.text)

    elif entered == 2:
        return