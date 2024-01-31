import requests
import sys
 
 
def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    else:
        try:
            quantity = float(sys.argv[1])
        except:
            sys.exit("Command-line argument is not a number")
        try:
            request = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        except requests.RequestException:
            pass
 
    data = request.json()
    price = float(data["bpi"]["USD"]["rate_float"])
    amount = price * quantity
    print(f"${amount:,.4f}")
 
if __name__ == "__main__":
    main()