from pyfiglet import Figlet
import sys
from random import choice

figlet = Figlet()


def main():
    choose_font()
    text = input("Input: ")
    print(f"Output: {figlet.renderText(text)}")


def choose_font():
    if len(sys.argv) == 1:
        f = choice(figlet.getFonts())
        figlet.setFont(font=f)



    elif len(sys.argv) == 3 and sys.argv[1] in ["-f","--font"] and sys.argv[2] in (figlet.getFonts()) :
        f = sys.argv[2]
        figlet.setFont(font=f)
        return f
    else:
        sys.exit("Invalid usage")

if __name__ == "__main__":
    main()
