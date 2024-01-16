def main():
    while True:
        try:
            numerator, denominator = input("Fraction: ").split("/")
            numerator, denominator = int(numerator), int(denominator)
            fraction = (numerator / denominator) * 100
            if fraction > 100:
                continue
            print(convert_value(fraction))
            break
        except (ValueError, ZeroDivisionError):
            pass
        


def convert_value(fraction):
    if 0 <= fraction <= 1:
        return "E"
    elif 99 <= fraction <= 100:
        return "F"
    elif 1 < fraction < 99:
        return str(int(round(fraction))) + "%"


if __name__ == "__main__":
    main()