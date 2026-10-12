def main():
    time = input("What Time is it? ")
    convert(time)
    meal_choice = convert(time)
    if meal_choice >= 7 and meal_choice <= 8:
        print("breakfast time")
    elif meal_choice >= 12 and meal_choice <= 13:
        print("lunch time")
    elif meal_choice >= 18 and meal_choice <= 19:
        print("dinner time")

def convert(time):
    period = time.split()[-1]
    hour, minute = time.split()[0].split(":")
    hour = int(hour)
    minute = int(minute)

    if period == "p.m." and hour != 12:
        hour += 12
    elif period == "a.m." and hour == 12:
        hour = 0
    time = float(((hour * 60) + minute) / 60)
    return time


if __name__ == "__main__":
    main()
