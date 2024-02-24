import sys
import csv
from tabulate import tabulate

def main():
    if len(sys.argv[1:]) < 1:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv[1:]) > 1:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")
    else:
        try:
            with open(f"{sys.argv[1]}") as file:
                reader = csv.reader(file)
                table = list(map(lambda row: row, reader))
        except FileNotFoundError:
            sys.exit("File does not exist")

        print(tabulate(table, headers="firstrow", tablefmt="grid"))

if __name__ == "__main__":
    main()