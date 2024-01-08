def main():
    mass_kg: int = int(input("m: "))
    c = 3 * 100000000
    E = mass_kg * c ** 2
    print(f"E: {E}")

main()