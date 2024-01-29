import random

def main():
    while True:
        try:
            level = int(input("Level: "))
            to_guest = random.randint(1, level + 1)
            break
        except:
            continue

    while True:
        try:
            number: int = int(input("Guess: "))
        except:
            continue
        if number > to_guest:
            print("Too large!")
            continue
        elif number < to_guest:
            print("Too small!")
            continue
        else:
            print("Just right!")
            break

if __name__ == "__main__":
    main()


