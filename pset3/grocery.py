groceries = {}
def main():
    input_items()
    for item in sorted(groceries):
        print(f"{groceries[item]} {item}")


def input_items():

    while True:
        try:
            item = input("").upper()
            if item in groceries:
                groceries[item] += 1
            else:
                groceries[item] = 1
        except EOFError:
            break




if __name__ == "__main__":
    main()
