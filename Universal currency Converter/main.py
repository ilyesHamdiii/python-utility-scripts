from dotenv import load_dotenv
import requests
import os
# i used FAST FOREX API 
load_dotenv()

def convert(amount, from_currency="TND", to_currency="USD"):
    api_key = os.getenv("API_KEY")

    if not api_key:
        print(" API_KEY not found in .env")
        return

    url = f"https://api.fastforex.io/fetch-one?from={from_currency}&to={to_currency}&api_key={api_key}"

    try:
        response = requests.get(url)
        data = response.json()

        if "error" in data:
            print(" API Error:", data["error"])
            return

        rate = data["result"][to_currency]
        converted = amount * rate

        print(f" {amount} {from_currency} = {converted:.2f} {to_currency} (Rate: {rate:.4f})")

    except Exception as e:
        print("Failed to fetch exchange:", e)


if __name__ == "__main__":

    amount = float(input("Enter amount: "))

    from_currency = input("From currency (e.g. TND): ").upper()

    to_currency = input("To currency (e.g. USD): ").upper()

    convert(amount, from_currency, to_currency)
