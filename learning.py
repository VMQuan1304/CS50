def main():
    print_square(3)

def print_columns(height: int = 1):
    print("#\n" * height, end="")

def print_row(width: int = 1):
    print("#" * width)

def print_square(size):
    for _ in range(size):
        print_row(4)

if __name__ == "__main__":
    main()