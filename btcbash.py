import requests
import time
import pyfiglet
import os

def get_btc_price():
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    response = requests.get(url)
    data = response.json()
    return data

try:
    while True:
        price = get_btc_price()["bpi"]["USD"]["rate_float"]
        current_time = get_btc_price()["time"]["updated"]

        while True:
            art = pyfiglet.figlet_format(f"{price:.2f}\033", font="smslant")

            os.system('clear')  # Clear the screen

            print(f"[{current_time}]")
            print(f"\033[93m1 ₿\033[0m = \033[92m$ {price:.2f}\033[0m")
            print(f"\033[92m{art}\033[0m")

            time.sleep(1)  # Wait for 1 second before fetching the price again

except KeyboardInterrupt:
    print("\n\033[91m[Ctrl+C] Exiting the program...\033[0m")
