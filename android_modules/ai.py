import requests


def _gemini_generate(api_key, message):
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent"
    headers = {
        "Content-Type": "application/json",
        "x-goog-api-key": api_key,
    }
    payload = {
        "contents": [
            {
                "parts": [
                    {"text": message}
                ]
            }
        ]
    }

    response = requests.post(url, headers=headers, json=payload, timeout=60)
    response.raise_for_status()
    data = response.json()

    candidates = data.get("candidates") or []
    if not candidates:
        raise RuntimeError("Gemini returned no response")

    parts = candidates[0].get("content", {}).get("parts", [])
    text_parts = [part.get("text", "") for part in parts if part.get("text")]
    if not text_parts:
        raise RuntimeError("Gemini returned an empty response")

    return "".join(text_parts)


def AI():
    try:
        with open("api_key_radmehr_os.txt", "r") as file:
            api = file.read().strip()
    except FileNotFoundError:
        api = ""

    if api == "":
        api = input("whats your api? ").strip()
        with open("api_key_radmehr_os.txt", "w") as file:
            file.write(api)

    print("1. chat with ai")
    print("2. exit")

    try:
        entered = int(input("choose choose!! "))
    except ValueError:
        print("Please enter a number!")
        return

    if entered == 1:
        while True:
            message = input("You: ")
            exit_words = ["خداحافظ", "بای", "goodbye", "bye"]
            if message in exit_words:
                print("Gemini: goodbye! 👋")
                break

            try:
                text = _gemini_generate(api, message)
                print("Gemini:", text)
            except requests.RequestException:
                print("get new api and turn on the vpn and back to ai!")
                return
            except (KeyError, ValueError, RuntimeError):
                print("Gemini returned an invalid response. Please try again.")
                return

    elif entered == 2:
        return
