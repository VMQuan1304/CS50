import sys

def main():
    is_valid(sys.argv)
    count_code_line(sys.argv[1])

def is_valid(argv):
    if len(argv[1:]) == 0:
        sys.exit("Too few command-line arguments")
    elif len(argv[1:]) >1 :
        sys.exit("Too many command-line arguments")
    elif not(argv[1].endswith(".py")):
        sys.exit("Not a Python file")
    else:
        return True
    
def count_code_line(file_path):
    try:
        with open(f"{file_path}") as file:
            readlines = file.readlines()
    except FileNotFoundError:
        sys.exit("File does not exist")
    line_total = sum(1 for line in readlines if is_code(line))
    print(line_total)

def is_code(line):
    return line.strip() and not line.lstrip().startswith("#")

if __name__ == "__main__":
    main()