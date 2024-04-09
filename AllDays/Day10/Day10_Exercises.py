# The goal of this program is to create a function with an output of the inputted name in titlecase.

# def format_name(fname, lname):
#     formFirstName = fname.title()
#     formLastName = lname.title()
#     return f"{formFirstName} {formLastName}"
#
#
# formFullName = format_name("jOHN", "DOe")
# print(formFullName)

# The goal of this program is to print the number of days in a month
# given the year and month taking leap years into account for February.
# While this version of the program DOES work, it is not the best way of doing so, I now realize


def is_leap(year):
    """Returns True or False if the given year is a leap year."""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leapYear = True
            else:
                leapYear = False
        else:
            leapYear = True
    else:
        leapYear = False
    return leapYear


def days_in_month(year, month):
    """Returns the number of days in a given month (input month number 1-12)."""
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year) == True:
        month_days[1] = 29
    returnDays = month_days[month - 1]
    return returnDays

year = int(input())
month = int(input())
days = days_in_month(year, month)
print(days)

