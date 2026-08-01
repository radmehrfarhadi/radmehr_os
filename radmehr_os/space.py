import requests
import webbrowser

def Space():
    # ۱. خواندن کلید فقط یک‌بار قبل از شروع حلقه برای بالا رفتن سرعت
    try:
        with open("nasa_api_key.txt") as file:
            api_key = file.read().strip()
    except FileNotFoundError:
        print("خطا: فایل nasa_api_key.txt پیدا نشد!")
        return

    while True:
        print("\n--- NASA Space Menu ---")
        print("1. Astronomy picture")
        print("2. Exit")

        try:
            choice = int(input("Choose: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:
            # یادآوری فرمت تاریخ به کاربر
            nasa_date = input("What day? (Format: YYYY-MM-DD, e.g., 2024-10-25): ")
            url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}&date={nasa_date}"
            
            try:
                response = requests.get(url)
                # بررسی اینکه آیا پاسخ سرور موفقیت‌آمیز بوده یا خیر (مثلا تاریخ اشتباه نبوده باشد)
                if response.status_code == 200:
                    data = response.json()
                    
                    # باز کردن عکس در مرورگر
                    webbrowser.open(data["url"])
                    
                    print(f"\nTitle: {data['title']}")
                    print(f"URL: {data['url']}")
                    print(f"\nExplanation:\n{data['explanation']}\n")
                else:
                    print(f"Error from NASA: {response.json().get('msg', 'Unknown error')}")
            except Exception as e:
                print(f"Connection error: {e}")
    
        elif choice == 2:
            print("Exiting Space module...")
            break # استفاده از break برای خروج درست از حلقه
        else:
            print("Invalid choice! Please choose 1 or 2.")


