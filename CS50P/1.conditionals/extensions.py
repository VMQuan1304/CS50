def main():
    fileEnd: str = input("File Name: ").lower().split(sep=".")[1]
    print(fileEnd)
    match fileEnd:
        case "jpg" | "png" | "jpeg":
            print(f"image/{fileEnd}")

main()