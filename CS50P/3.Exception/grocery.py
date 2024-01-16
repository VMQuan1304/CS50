def main():
    dict = {}
    key = 0
    while True:
        try:
            key = input().strip()
            if key in dict:
                dict[key] += 1
            else:
                dict[key] = 1 
        except EOFError:
            break
    print("\n")
    for key, value in sorted(dict.items()):
        print(value, key.upper())

if __name__ == "__main__":
    main()