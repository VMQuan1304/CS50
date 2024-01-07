def main():
    expression: str = input("Expression: ")

    x, y, z = expression.split(" ")
    x_float, z_float = float(x), float(z)

    match y:
        case "+":
            print(x_float + z_float)
        case "-":
            print(x_float - z_float)
        case "*":
            print(x_float * z_float)
        case "/":
            print(x_float / z_float)

if __name__ == "__main__":
    main()