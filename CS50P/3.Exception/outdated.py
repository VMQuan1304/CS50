months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    while True:
        try:
            user_input = input("Date: ").strip().title()
            if "/" in user_input:
                month, day, year = user_input.split("/")
            elif "," in user_input:
                month, day, year = user_input.replace(",", "").split()
                month = months.index(month) + 1
            else:
                continue
            month, day = int(month), int(day)
            if 1 <= month <= 12 and 1 <= day <= 31:
                break
        except ValueError:
            pass
    
    print(f"{year:04}-{month:02}-{day:02}")


if __name__ == "__main__":
    main()