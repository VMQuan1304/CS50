import sys, os
from PIL import Image, ImageOps


def main():
    if is_valid(sys.argv):
        overlay(sys.argv[1], sys.argv[2])

def is_valid(argv):
    supported_file = ((".jpg", ".jpeg", ".png"))
    file_1, ext_1 = os.path.splitext(argv[1].lower())
    file_2, ext_2 = os.path.splitext(argv[2].lower())
    if len(argv[1:]) < 2:
        sys.exit("Too few command-line arguments")
    elif len(argv[1:]) > 2:
        sys.exit("Too many command-line arguments")
    elif not ext_1.endswith(supported_file):
        sys.exit("Invalid input")
    elif not ext_2.endswith(supported_file):
        sys.exit("Invalid output")
    elif ext_1 != ext_2:
        sys.exit("Input and output have different extensions")
    else:
        return True
    
def overlay(input_path, output_path):
    shirt = Image.open("shirt.png")
    input = Image.open(f"{input_path}")
    input = ImageOps.fit(input, shirt.size)
    input.paste(shirt, shirt)
    input.save(f"{output_path}")

if __name__ == "__main__":
    main()