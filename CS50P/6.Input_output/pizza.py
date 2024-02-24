import sys, csv
from tabulate import tabulate

def main():
    if is_valid(sys.argv):
        print_tabulate(sys.argv[1])

def is_valid(argv):
    if len(argv[1:]) == 0:
        sys.exit("Too few command-line arguments")
    elif len(argv[1:]) >1 :
        sys.exit("Too many command-line arguments")
    elif not(argv[1].endswith(".csv")):
        sys.exit("Not a CSV file")
    else:
        return True
    
def print_tabulate(file_path):
    try:
        with open(f"{file_path}") as file:
            reader = csv.reader(file)
            table = list(map(lambda row: row, reader))
    except FileNotFoundError:
        sys.exit("File does not exist")

    print(tabulate(table, headers="firstrow", tablefmt="grid"))

if __name__ == "__main__":
    main()