from enum import Enum


class month(Enum):
    January = 1
    February = 2
    March = 3
    April = 4
    May = 5
    June = 6
    July = 7
    August = 8
    September = 9
    October = 10
    November = 11
    December = 12


class season(Enum):
    Winter = 1
    Spring = 2
    Summer = 3
    Autumn = 4


while True:
    while True:
        try:
            s = int(input('month:'))
            break
        except ValueError:
            print('Number of month')
    if s in range(1, 3):
        print('Winter')
    elif s in range(3, 6):
        print('Spring')
    elif s in range(6, 9):
        print('Summer')
    elif s in range(9, 12):
        print('Autumn')
    elif s == 12:
        print('Winter')
    print(f'If you want to exit {exit}')
    leave = input()
    if leave == 'exit':
        break
