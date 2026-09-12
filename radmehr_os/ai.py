from google import genai
import google

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
            exit_words = ["خداحافظ", "بای", "goodbye", "bye"]
            if message in exit_words:
                print("Gemini: goodbye! 👋")
                break
            try:
                response = client.models.generate_content(
                    model="gemini-3.5-flash",
                    contents=message
                )
            except google.genai.errors.ClientError:
                print("get new api and tern on the vpn and back to ai!")
                return
            print("Gemini:", response.text)

    elif entered == 2:
        return