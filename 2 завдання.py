from enum import Enum


class converter(Enum):
    USD = 1
    EUR = 2
    CZK = 3
    PLN = 4


while True:
    while True:
        try:
            x = float(input('amount of money:'))
            p = converter[input('currency:')]
            break
        except ValueError:
            print('Введіть числа:')
    if p == converter.USD:
        x = x / 24.58
        print(f'Гроші в USD {x}')
    elif p == converter.EUR:
        x = x / 26.91
        print(f'Гроші в EUR {x}')
    elif p == converter.CZK:
        x = x / 1.08
        print(f'Гроші в CZK {x}')
    elif p == converter.PLN:
        x = x / 6.31
        print(f'Гроші в PLN {x}')
    print(f'If you want to exit {exit}')
    leave = input()
    if leave == 'exit':
        break
