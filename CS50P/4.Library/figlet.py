import sys
from pyfiglet import Figlet
import random as rd

def main():
    figlet = Figlet()
    if len(sys.argv) == 1:
        f = rd.choice(figlet.getFonts())
        figlet.setFont(font=f)
    elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"]:
        try:
            figlet.setFont(font=sys.argv[2])
        except:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")

    s = input("Input: ")
    print(figlet.renderText(s))

if __name__ == "__main__":
    main()