def main():
    while True:
        try:
            numerator, denominator = input("Fraction: ").split("/")
            numerator, denominator = int(numerator), int(denominator)
            fraction = (numerator / denominator) * 100
            break
        except (ValueError, ZeroDivisionError):
            pass
    if fraction <= 1:
        fraction = "E"
    elif fraction >= 99:
        fraction = "F"
    else:
        fraction = str(int(fraction)) + "%"
    
    print(f"{fraction}")

if __name__ == "__main__":
    main()