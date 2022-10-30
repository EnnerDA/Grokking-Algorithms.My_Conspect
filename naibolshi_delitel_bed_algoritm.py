def nod(a,b):
    if b > a:
        a, b = b, a
    if a == b:
        print(f'наибольший общий делитель {b}')
    elif a > b:
        if a % b == 0:
            print(f' наибольший общий делитель {b}')
        else:
            flag = False
            i = 1
            while flag == False:
                i += 1
                print(i, b/i, a%(b/i))
                if b / 1 < 1:
                    print(f'Нет делителя')
                    flag = True                    
                elif b % i == 0 and a % (b/i) == 0:
                    print(f'наибольший общий делитель {b/i}')
                    flag = True
                elif b/i <= 1:
                    print(f'Нет делителя')
                    flag = True
