def main():
    fileEnd: str = input("File Name: ").lower().strip().split(sep=".")[-1]
    match fileEnd:
        case "jpg" | "jpeg":
            print(f"image/jpeg")
        case "png" | "gif":
            print(f"image/{fileEnd}")
        case "pdf" | "zip":
            print(f"application/{fileEnd}")
        case "txt":
            print(f"text/plain")
        case "bin" | _:
            print("application/octet-stream")

if __name__ == "__main__":
    main()