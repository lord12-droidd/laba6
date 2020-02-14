days = range(1, 32)
months = range(1, 13)
years = range(1901, 2020)
d31 = [1, 3, 5, 7, 8, 10, 12]
d30 = [4, 6, 9, 11]
d28 = [2]
a = range(1900, 2024, 4)
while True:
    while True:
        try:
            d, m, y = int(input('day:')), \
                      int(input('month:')), \
                      int(input('year:'))
            k = [d, m, y]
            dc = k[0]
            mc = k[1]
            yc = k[2]
            break
        except ValueError:
            print(f'Input digital date')
    if d not in days or m not in months or y not in years:
        print('Invalid date')
    if m in d31 and 1 <= d <= 31 and y in years:
        d = d + 1
        if d == 32 and m == 12:
            y = y + 1
        if d == 32:
            d = 1
            m = m + 1
            if m >= 13:
                m = 1
        print(f'Next: Day:{d} month:{m} year:{y}')
        dc = dc - 1
        if dc <= 0 and mc == 1:
            yc = yc - 1
        if dc <= 0:
            mc = mc - 1
            if dc <= 0 and mc == 0:
                dc = 31
                mc = 12
        elif dc == 30 and mc == 12:
            dc = 30
            mc = 12
        if dc <= 0 and mc in d31:
            dc = 31
            if m == 0:
                m = 12
        if dc <= 0 and mc in d30:
            dc = 30
            if m == 0:
                m = 12
        if dc <= 0 and mc in d28 and y in a:
            dc = 29
            if m == 0:
                m = 12
        if dc <= 0 and mc in d28:
            dc = 28
            if m == 0:
                m = 12
        print(f'Previous: day {dc} month {mc} year:{yc}')
    elif m in d30 and 1 <= d <= 30 and y in years:
        d = d + 1
        if d == 31:
            d = 1
            m = m + 1
            if m > 13:
                m = 1
        print(f'Next: Day:{d} month:{m} year:{y}')
        dc = dc - 1
        if dc <= 0:
            mc = mc - 1
        if dc <= 0 and mc in d30:
            dc = 30
            mc = mc - 1
            if m == 0:
                m = 12
        if dc <= 0 and mc in d31:
            dc = 31
            if m == 0:
                m = 12
        if dc <= 0 and mc in d28:
            dc = 28
            if m == 0:
                m = 12
        print(f'Previous: day {dc} month {mc} year:{y}')
    elif m in d28 and 1 <= d <= 29 and y in a and y in years:
        d = d + 1
        if d == 30:
            d = 1
            m = m + 1
            if m > 13:
                m = 1
        print(f'Next: Day:{d} month:{m} year:{y}')
        dc = dc - 1
        if dc <= 0:
            mc = mc - 1
        if dc <= 0 and mc in d30:
            dc = 30
            mc = mc - 1
            if m == 0:
                m = 12
        if dc <= 0 and mc in d31:
            dc = 31
            if m == 0:
                m = 12
        if dc <= 0 and mc in d28:
            dc = 28
            mc = mc - 1
            if m == 0:
                m = 12
        print(f'Previous: day {dc} month {mc} year:{y}')
    elif m in d28 and 1 <= d <= 28 and y not in a and y in years:
        d = d + 1
        if d == 29:
            d = 1
            m = m + 1
            if m > 13:
                m = 1
        print(f'Next: Day:{d} month:{m} year:{y}')
        dc = dc - 1
        if dc <= 0:
            mc = mc - 1
        if dc <= 0 and mc in d30:
            dc = 30
            mc = mc - 1
            if m == 0:
                m = 12
        if dc <= 0 and mc in d31:
            dc = 31
            if m == 0:
                m = 12
        if dc <= 0 and mc in d28:
            dc = 27
            mc = mc - 1
            if m == 0:
                m = 12
        print(f'Previous day: {dc} month {mc} year:{y}')
    print(f'If you want to exit {exit}')
    leave = input()
    if leave == 'exit':
        break
