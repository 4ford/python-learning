import inflect

p = inflect.engine()


def main():
    names = get_names()
    print(f"Adieu, adieu, to {p.join(names)}")


def get_names():
    names = []
    while True:
        try:
            names.append(input("Name: "))
        except EOFError:
            print()
            return names


if __name__ == "__main__":
    main()
