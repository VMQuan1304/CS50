import inflect

def main():
    name_list = []
    while True:
        try:
            s = input("Name: ")
            name_list.append(s)
            p = inflect.engine().join(name_list)
        except EOFError:
            print(f"\nAdieu, adieu, to {p}")
            break

if __name__ == "__main__":
    main()