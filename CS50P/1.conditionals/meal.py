def main() -> str:
    time: str = input("What time is it? ").strip()
    hours: float = convert(time)
    if 7.0 <= hours <= 8.0:
        print("Breakfast Time")
    elif 12.0 <= hours <= 13.0:
        print("Lunch Time")
    elif 18.0 <= hours <= 19.0:
        print("Dinner Time")
    else:
        print("")


def convert(time: str = "7:30") -> float:
    hours_str, minutes_str = time.split(":")
    hours_float, minutes_float = (float(hours_str), float(minutes_str))
    return hours_float + minutes_float / 60


if __name__ == "__main__":
    main()