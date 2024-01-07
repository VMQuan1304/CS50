def main():
    user_input: str = input("Input: ")
    print("Output: ", vowels_omit(user_input))

def vowels_omit(letters: str) -> str:
    letters_omitted = ""
    for letter in letters:
        if letter.lower() not in set("aeiou"):
            letters_omitted += letter
    return letters_omitted

if __name__ == "__main__":
    main()