def main():
    amount_due = 50
    while amount_due > 0:
        user_input: int = int(input("Insert Coin: "))
        amount_due: int = money_cal(user_input, amount_due)
        if amount_due > 0:
            print("Amount Due: ", amount_due, sep="")
        else:
            print("Change Owed: ", abs(amount_due), sep="")

def money_cal(inserted_coin: int, amount_due: int) -> int:
    if inserted_coin in [5, 10, 25]:
        amount_due -= inserted_coin
    return amount_due

if __name__ == "__main__":
    main()