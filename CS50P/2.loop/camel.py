def main() -> str:
    user_input = input("camelCase: ")
    print(snake_case_func(user_input))

def snake_case_func(camelCase: str = "camelCaseStr") -> str:
    snake_case = ""
    for letter in camelCase:
        if letter.isupper():
            snake_case += "_"
        snake_case += letter
    return snake_case.lower()

if __name__ == "__main__":
    main()