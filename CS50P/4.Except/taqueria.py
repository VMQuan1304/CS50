menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    total_bill = 0
    while True:
        try:
            user_input = input("Item: ").title().strip()
        except EOFError:
            print("\n")
            break
        if user_input in menu:
            price = menu[user_input]
            total_bill += price
            print(f"Total: ${total_bill:0.2f}")

if __name__ == "__main__":
    main()