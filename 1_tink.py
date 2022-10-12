while True:
    #'Обработаем возможные ошибки, которые могут появиться при вводе параметров'
    try:
        parametrs = []
        for i in input(f'Введите через "пробел" четыре неотрицательных различных целых числа a, b, x, y a,b,x,y \n'
              f'начальная и конечная точки маршрута, а также описание экспресса (0 <= a,b,x,y <= 10^9): ').split():
            if int(i) >= 1 and int(i) <= (10 ** 9):
                parametrs.append(int(i))
                is_null = 100 / int(i)
            elif int(i) > 10 ** 9:
                print('Ни один из параметров не должен превышать 10^9')
                break
            elif int(i) <= 0:
                print('Ни один из параметров не может быть <= 0!')
                break
        if len(parametrs) != 4:
            print("Вы ввели неверное количество параметров, их должно быть 4! Повторите ввод!")
            continue
        break

    except ValueError:
        print('Вы ввели не число / не целое число!')



var_1 = abs(int(parametrs[0]) - int(parametrs[1]))
var_2 = abs(int(parametrs[0]) - int(parametrs[2])) + abs(int(parametrs[3]) - int(parametrs[1]))
var_3 = abs(int(parametrs[0]) - int(parametrs[3])) + abs(int(parametrs[2]) - int(parametrs[1]))

possible_variants = [var_1, var_2, var_3]

print(min(possible_variants))