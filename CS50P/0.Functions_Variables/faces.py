def main():
    user_input: str = input()
    print(convert(user_input))

def convert(input_str: str = "") -> str:
    converted_str = input_str.replace(":)", "🙂").replace(":(", "🙁")
    return converted_str

main()