import emoji as e

def main():
    user_input = input("Input: ")
    print(e.emojize(user_input, language="alias"))


if __name__ == "__main__":
    main()