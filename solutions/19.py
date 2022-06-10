
year = 1900
day = 0
months_regular = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
months_leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

sunday_count = 0

while year < 2001:
    leapyear = False
    if year % 100 == 0:
        if year % 400 == 0:
            leapyear = True
    else:
        if year / 4 == year // 4:
            leapyear = True
    if leapyear:
        months = months_leap
    else:
        months = months_regular
    month_count = 0
    while month_count < 12:
        month_days = 0
        if year >= 1901 and day == 6:
            sunday_count += 1
        while month_days < months[month_count]:
            day = (day + 1) % 7
            month_days += 1
        month_count += 1
    year += 1
    
print(sunday_count)
    