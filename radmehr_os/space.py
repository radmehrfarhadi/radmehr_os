import requests
import webbrowser

def Space():
    while True:
        print("1. Astronomy picture")
        print("2. Exit")

        choice = int(input("choose: "))

        with open("nasa_api_key.txt") as file:
            api_key = file.read().strip()
        url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"


        if choice == 1:
            nasa_date = input("What day? ")
            url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}&date={nasa_date}"
            response = requests.get(url)
            data = response.json()
            webbrowser.open(data["url"])
            print(data["title"])

            print()

            print("URL:")
            print(data["url"])

            print()

            print("Explanation:")
            print(data["explanation"])
    
        elif choice == 2:
            return