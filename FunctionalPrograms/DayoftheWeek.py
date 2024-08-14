
# This program takes a date as input and returns the day of the week for that date.
def dayof_week(month,day,year):
    """This function takes the month, day, and year as input and returns the day of the week for that date.
    The function uses Zeller's Congruence to calculate the day of the week.
    Args:
        month (int): The month of the date.
        day (int): The day of the date.
        year (int): The year of the date.
        Returns:
        int: The day of the week for the date."""

    year = year - (14 - month) // 12
    date = year + year // 4 - year // 100 + year // 400
    month = month + 12 * ((14 - month) // 12) - 2
    day = (day + date + (31 * month) // 12) % 7
    return day


def main():
    """This function takes the month, day, and year as input and prints the day of the week for that date.
    The function uses the dayof_week function to calculate the day of the week.
    Args:
        None
        Returns:
        None"""

    month = int(input("Enter the month: "))
    day = int(input("Enter the day: "))
    year = int(input("Enter the year: "))
    day_of_week = dayof_week(month, day, year)
    if day_of_week == 0:
        print("Sunday")
    elif day_of_week == 1:
        print("Monday")
    elif day_of_week == 2:
        print("Tuesday")
    elif day_of_week == 3:
        print("Wednesday")
    elif day_of_week == 4:
        print("Thursday")
    elif day_of_week == 5:
        print("Friday")
    elif day_of_week == 6:
        print("Saturday")

main()