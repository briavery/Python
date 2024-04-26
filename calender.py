import calendar, datetime

def main():
    try:
        current_year = datetime.datetime.now().year
        birthmonth = int(input("Please enter your birth month (1-12): "))

        if(not 0<birthmonth<13):
            raise ValueError("Birthmonth is not an integer within the range.")

        cal = calendar.monthcalendar(current_year, birthmonth)

        # Print the header
        print(calendar.month_name[birthmonth], current_year)
        print("Mo Tu We Th Fr Sa Su")

        # Print each week
        for week in cal:
            for day in week:
                if day == 0:
                    print("   ", end=" ")  # Print empty space for days outside the month
                else:
                    print(f"{day:2d} ", end=" ")
            print()

    except ValueError as e:
        print("Error:", e)

main()