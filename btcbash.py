import requests
import time
import pyfiglet
import os

def get_btc_price():
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return None
    except ValueError as e:
        print(f"Error parsing data: {e}")
        return None

try:
    while True:
        data = get_btc_price()
        if data:
            price = data["bpi"]["USD"]["rate_float"]
            current_time = data["time"]["updated"]

            art = pyfiglet.figlet_format(f"{price:.2f}", font="smslant")

            os.system('clear')  # Clear the screen

            print(f"[{current_time}]")
            print(f"\033[93m1 ₿\033[0m = \033[92m$ {price:.2f}\033[0m")
            print(f"\033[92m{art}\033[0m")
        time.sleep(10)  # Wait for 1 seconds before fetching the price again

except KeyboardInterrupt:
    print("\n\033[91m[Ctrl+C] Exiting the program...\033[0m")
