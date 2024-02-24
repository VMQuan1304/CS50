import sys

def main():
    if len(sys.argv[1:]) == 0:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv[1:]) >1 :
        sys.exit("Too many command-line arguments")
    elif not(sys.argv[1].endswith(".py")):
        sys.exit("Not a Python file")
    else:
        try:
            with open(f"{sys.argv[1]}") as file:
                readlines = file.readlines()
        except FileNotFoundError:
            sys.exit("File does not exist")
        line_total = sum(1 for line in readlines if is_code(line))
        print(line_total)


def is_code(line):
    return line.strip() and not line.lstrip().startswith("#")

if __name__ == "__main__":
    main()