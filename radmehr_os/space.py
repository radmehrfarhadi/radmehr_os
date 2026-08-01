import requests
import webbrowser


def Space():
    try:
        with open("nasa_api_key.txt") as file:
            api_key = file.read().strip()

    except FileNotFoundError:
        print("Error: nasa_api_key.txt not found!")
        return

    while True:
        print("\n--- NASA Space Menu ---")
        print("1. Astronomy picture")
        print("2. Exit")
        print("3. ISS location")

        try:
            choice = int(input("Choose: "))

        except ValueError:
            print("Please enter a valid number.")
            continue


        if choice == 1:
            nasa_date = input(
                "What day? (Format: YYYY-MM-DD, example: 2026-07-31): "
            )

            url = (
                f"https://api.nasa.gov/planetary/apod"
                f"?api_key={api_key}&date={nasa_date}"
            )

            try:
                response = requests.get(url)
                data = response.json()

                if response.status_code == 200:
                    webbrowser.open(data["url"])

                    print("\nTitle:")
                    print(data["title"])

                    print("\nURL:")
                    print(data["url"])

                    print("\nExplanation:")
                    print(data["explanation"])

                else:
                    print("NASA Error:")
                    print(data.get("msg"))

            except Exception as e:
                print("Connection error:", e)



        elif choice == 3:
            url2 = "http://api.open-notify.org/iss-now.json"

            try:
                response = requests.get(url2)
                data = response.json()

                lat = data["iss_position"]["latitude"]
                lon = data["iss_position"]["longitude"]

                print("\nISS Location:")
                print("Latitude:", lat)
                print("Longitude:", lon)

                google_maps_url = (
                    f"https://www.google.com/maps?q={lat},{lon}"
                )

                webbrowser.open(google_maps_url)

            except Exception as e:
                print("ISS API error:", e)



        elif choice == 2:
            print("Exit Space module...")
            break


        else:
            print("Invalid choice!")