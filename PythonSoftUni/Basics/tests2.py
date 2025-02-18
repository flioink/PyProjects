from datetime import date


def eval_date():
    time_frame = input("Enter a date in the format YYYY-MM-DD: ")

    # Parse the given date string into year, month, and day components
    year_to_check, month_to_check, day_to_check = map(int, time_frame.split("-"))

    # Get the current date
    current_date = date.today()

    # Compare the given date with the current date
    if current_date == date(year_to_check, month_to_check, day_to_check):
        print("Today's date")
    elif current_date > date(year_to_check, month_to_check, day_to_check):
        print("Passed")
    else:
        days_remaining = (date(year_to_check, month_to_check, day_to_check) - current_date).days
        print(f"{days_remaining} days remaining")


eval_date()
