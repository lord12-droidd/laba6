while True:
    while True:
        try:
            t = int(input('Time = '))
            break
        except ValueError:
            print('Only numbers')
    if 0 < t <= 60:
        if 0 < t % 6 <= 3:
            print('Green light')
        elif t % 6 == 4:
            print('Yellow light')
        else:
            print('Red light')
    else:
        print('Wrong time. It must be in range from 0 to 60')
    print(f'If you want to exit {exit}')
    leave = input()
    if leave == 'exit':
        break