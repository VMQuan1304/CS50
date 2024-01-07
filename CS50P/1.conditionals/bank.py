def main() -> str:
    greeting: str = input("Greeting: ").lower()
    if greeting.startswith("hello"):
        print_out = "$0"
    elif greeting.startswith("h"):
        print_out = "$20"
    else:
        print_out = "$100"
    print(print_out)

main()