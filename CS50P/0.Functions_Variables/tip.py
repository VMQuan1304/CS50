def main():
    dollars_float = dollars_to_float(input("How much was the meal? "))
    percent_float = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars_float * percent_float
    print(f"Leave ${tip:.2f}")


def dollars_to_float(dollars: str) -> float:
    dollars_float: float = float(dollars.removeprefix("$"))
    return dollars_float

def percent_to_float(percent:str) -> float:
    percent_float: float = float(percent.removesuffix("%")) / 100
    return percent_float

main()