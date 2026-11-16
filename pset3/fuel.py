#Take a fraction
#Convert into a percent and print
#If percent >= 99% print E
#If percent <= print E


def main():
    percentage = fuel_percent()   # catches the returned value
    gauge(percentage)


def fuel_percent():
    while True:
        try:
            x, y = input("Fraction: ").split("/")
            x, y = int(x), int(y)
            if x > y or x < 0:
                continue
            return round(x / y * 100)
        except (ValueError, ZeroDivisionError):
            pass
def gauge(percentage):
    if percentage >= 99 and percentage <= 100:
        print("F")
    elif percentage >= 0 and percentage <= 1:
        print("E")
    else:
        print(f"{percentage}%")
#
#  Split the string into two parts


# Do the math straight up by converting them to integers on the fly
#percentage = (int(parts[0]) / int(parts[1])) * 100

#print(f"{percentage}%")  # Output: 75.0%

main()

