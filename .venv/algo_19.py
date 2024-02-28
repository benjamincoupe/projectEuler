"""

Problem 19: Counting Sundays

You are given the following information, but you may prefer to do some research for yourself.

    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

"""

def countingSundays(firstYear, lastYear):

    week_day = 1
    sundays = 0

    for year in range(1901, lastYear+1):

        for month in range(0, 12):
            if month==3 or month == 5 or month == 8 or month == 10:
                num_days = 30
            elif month==1:
                if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
                    num_days = 29
                else:
                    num_days = 28
            else:
                num_days = 31

            for month_day in range(0, num_days):

                if month_day == 0 and week_day % 7 == 0 and year in range(firstYear, lastYear):
                    sundays += 1
                week_day += 1

    return sundays








print(countingSundays(1943, 1946))
print(countingSundays(1995, 2000))
print(countingSundays(1901, 2000))
#     1 Jan 1900 was a Monday