import sys
import csv

def main():
    if is_valid(sys.argv):
        write_csv(sys.argv[1], sys.argv[2])

def is_valid(argv):
    if len(argv[1:]) < 2:
        sys.exit("Too few command-line arguments")
    elif len(argv[1:]) > 2:
        sys.exit("Too many command-line arguments")
    elif not argv[1].endswith(".csv"):
        sys.exit(f"{argv[1]} is not a CSV file")
    else:
        return True

def write_csv(input, output):
    try:
        with open(f"{input}") as input:
            reader = csv.DictReader(input)
            with open(f"{output}", "w", newline="") as output:
                writer = csv.DictWriter(output, fieldnames=["first", "last", "house"])

                writer.writeheader()

                for row in reader:
                    last, first = row["name"].split(", ")
                    writer.writerow({"first": first, "last": last, "house": row["house"]})

    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

if __name__ == "__main__":
    main()