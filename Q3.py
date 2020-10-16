# Name : Ida Bagus Ryogassa Avatara
# ID   : 2440100323


import calendar


def date(year, month):
    return calendar.month(year, month, w=0, l=0)


if __name__ == "__main__":
    month = int(input("Enter a Month: "))
    year = int(input("Enter a Year: "))
    print(date(year, month))
