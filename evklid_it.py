def evklid_it(a, b):
    if a < 0 or b < 0:
        print('NO!!!!')
    if a == b:
        print(f'Наибольший общий делитель {a}')
    if b > a:
        a,b = b,a
    if a > b:
        if a % b == 0:
            print(f'Наибольший общий делитель {b}')
        else:
            c = a%b
            evklid_it(b,c)
