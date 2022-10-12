while True:
    #'Обработаем возможные ошибки, которые могут появиться при вводе параметров'
    try:
        default_rectangle = []
        for i in input(f'Введите через "пробел" параметры исходного прямоуголника H и W,\n'
                       f'принадлежащих диапозону от 1 до 10^9 включительно: ').split():
            if int(i) >= 0 and int(i) <= (10 ** 9):
                default_rectangle.append(int(i))
                default_rectangle.sort()
                is_null = 100 / int(i)
            elif int(i) > 10 ** 9:
                print('Сторона прямоугольника не должна превышать 10^9')
                break
            else:
                print('Сторона прямоугольника не может быть отрицательной!')
                break
        if len(default_rectangle) != 2:
            print("Вы ввели неверное количество параметров, их должно быть 2! Либо один из параметров не допустим. Повторите ввод!")
            continue
        break

    except ValueError:
        print('Вы ввели не число / не целое число!')

    except ZeroDivisionError:
        print('Сторона прямоугольника не может быть равна 0!')


while True:
    # 'Обработаем возможные ошибки, которые могут появиться при вводе параметров'
    try:
        require_rectangle = []
        for i in input(f'Введите через "пробел" параметры исходного прямоуголника h и w,\n'
                       f'принадлежащих диапозону от 1 до 10^9 включительно: ').split():
            if int(i) >= 0 and int(i) <= (10 ** 9):
                require_rectangle.append( int(i) )
                require_rectangle.sort()
                is_null = 100 / int(i)
            elif int(i) > 10 ** 9:
                print('Cторона прямоугольника не должна превышать 10^9')
                break
            else:
                print('Сторона прямоугольника не может быть отрицательной!')
                break
        if len(require_rectangle) != 2:
            print("Вы ввели неверное количество параметров, их должно быть 2! Либо один из параметров не допустим. Повторите ввод!")
            continue
        break

    except ValueError:
        print('Вы ввели не число / не целое число!')

    except ZeroDivisionError:
        print('Сторона прямоугольника не может быть равна 0!')

#'Если параметры исходного и требуемого прямоугольников равны, то кол-во сгибов будет равно 0'
if default_rectangle == require_rectangle:
    fold_count = 0
# Если хотя бы один из парметров требуемого прямоугольника будет превышать все значения длин исходного прямоугольника,
# то такой прямоугольник не получится сделать
elif min(require_rectangle) > min(default_rectangle) or max(require_rectangle) > max(default_rectangle):
        fold_count = -1

else:
    fold_count = 0
    index = list(range(len(default_rectangle)))
    for i in index:
        # если требуемая длина больше исходной более, чем в 2 раза и не равна 1, то сначала нужно максимально сократить
        # эту сторону, а именно сложить ее вдвое, делаем это циклом
        while (default_rectangle[i] / require_rectangle[i]) > 2:
            fold_count += 1
            default_rectangle[i] = default_rectangle[i] / 2
        #иначе просто складываем до требуемого размера
        else:
            fold_count += 1


print((fold_count))
