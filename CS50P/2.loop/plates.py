import string

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s) -> bool:
    if len(s) < 2 or len(s) > 6:
        return False

    if not(s.isalnum()) or s.isdigit():
        return False

    first_num_index = 0
    for i, letter in enumerate(s):
        if letter.isdigit():
            first_num_index = i
            if not s[first_num_index:].isdigit():
                return False
            break
        
    if s[first_num_index] == "0":
        return False
        
    return True

if __name__ == "__main__":
    main()