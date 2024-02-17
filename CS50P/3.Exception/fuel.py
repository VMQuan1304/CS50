def main():
    while True:
        fraction = input("Fraction: ")
        percentage = convert(fraction)
        if percentage in ["ValueError", "ZeroDivisionError"]:
            continue
        elif percentage > 100:
            continue
        else:
            print(gauge(percentage))
            break
        
def convert(fraction):
    try:
        numerator, denominator = fraction.split("/")
        numerator, denominator = int(numerator), int(denominator)
    except ValueError:
        return "ValueError"
    try:
        numerator / denominator 
    except ZeroDivisionError:
        return "ZeroDivisionError"
    return round(((numerator / denominator) * 100), 0)
        

def gauge(percentage):
    if 0 <= percentage <= 1:
        return "E"
    elif 99 <= percentage <= 100:
        return "F"
    elif 1 < percentage < 99:
        return str(int(round(percentage))) + "%"


if __name__ == "__main__":
    main()