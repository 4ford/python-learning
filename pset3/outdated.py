months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


def main():
    month, day, year = iso()
    print(f"{year}-{month:02}-{day:02}")

def iso():
    while True:
        try:
            date = input("Date: ")
            if "/" in date:
                month, day, year = date.split("/")
                month = int(month)
                day = int(day)
                year = int(year)
            else:
                month, day, year = date.split(" ")
                month = months.index(month) + 1
                if  not day.endswith(","):
                    raise ValueError
                day = int(day.replace(",", ""))
                year = int(year)

            if month < 1 or month > 12 or day < 1 or day > 31:
                raise ValueError
            else:
                return month, day, year
        except ValueError:
            continue
if __name__ == "__main__":
    main()
