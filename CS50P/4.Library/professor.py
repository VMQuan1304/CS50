import random


def main():
    level = get_level()
    point = 0
    for _ in range(10):
        a = generate_integer(level)
        b = generate_integer(level)
        i = 0
        while i < 2:
            i += 1
            try:
                result = int(input(f"{a} + {b} = "))
                if result == a + b:
                    point += 1
                    break
                else:
                    print("EEE")
                    continue
            except:
                print("EEE")
                continue
        if i == 2:
            print(f"{a} + {b} =", a + b)
    print(f"Score: {point}")

def get_level():
    while True:
        try:
            level = int(input("Level: "))
        except:
            continue
        if level in (1, 2, 3):
            return level


def generate_integer(level):
    if level == 1:
        return random.randint(0, 10)
    elif level == 2:
        return random.randint(10, 100)
    else:
        return random.randint(100, 1000)


if __name__ == "__main__":
    main()