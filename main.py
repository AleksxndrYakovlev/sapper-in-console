import os
import random


# Функция очистки консоли
def clear():
    os.system('cls')


# Функция для распечатки поля
def print_field(f, bool_f, f_size):
    count = 0

    # Вверхняя строка с номерами столбцов
    print('№  |', end='')
    for num in range(1, f_size + 1):
        if num >= 10:
            print(f' {num}|', end='')
        else:
            print(f' {num} |', end='')
    print('')
    for num in range(f_size + 1):
        print('----', end='')
    print('')

    # Распечатка строк
    for string in f:
        count += 1
        if count < 10:
            print(count, end='  ')
        else:
            print(count, end=' ')
        cell = 0
        for item in string:
            cell += 1
            if bool_f[count - 1][cell - 1] == True:
                print('|' + item, end='')
            else:
                print('|   ', end='')
        print('|')
        for num in range(f_size + 1):
            print('----', end='')
        print('')


# Открываем ячейки вокруг, если пользователь открыл ячейку с нулём
def open_around_zero(string_index, cell_index, bool_f, f_size):
    '''
    :param string_index:
    :param cell_index:
    :param bool_f:
    :param f_size:
    :return:
    '''
    if (string_index > 0) and (cell_index > 0):
        if not bool_f[string_index - 1][cell_index - 1]:
            bool_f[string_index - 1][cell_index - 1] = True
            if field[string_index - 1][cell_index - 1] == ' 0 ':
                open_around_zero(string_index - 1, cell_index - 1, bool_f, f_size)
        if not bool_f[string_index - 1][cell_index]:
            bool_f[string_index - 1][cell_index] = True
            if field[string_index - 1][cell_index] == ' 0 ':
                open_around_zero(string_index - 1, cell_index, bool_f, f_size)
        if not bool_f[string_index][cell_index - 1]:
            bool_f[string_index][cell_index - 1] = True
            if field[string_index][cell_index - 1] == ' 0 ':
                open_around_zero(string_index, cell_index - 1, bool_f, f_size)
        try:
            bool_f[string_index - 1][cell_index + 1] = bool_f[string_index - 1][cell_index + 1]
        except IndexError:
            pass
        else:
            if not bool_f[string_index - 1][cell_index + 1]:
                bool_f[string_index - 1][cell_index + 1] = True
                if field[string_index - 1][cell_index + 1] == ' 0 ':
                    open_around_zero(string_index - 1, cell_index + 1, bool_f, f_size)
        try:
            bool_f[string_index][cell_index + 1] = bool_f[string_index][cell_index + 1]
        except IndexError:
            pass
        else:
            if not bool_f[string_index][cell_index + 1]:
                bool_f[string_index][cell_index + 1] = True
                if field[string_index][cell_index + 1] == ' 0 ':
                    open_around_zero(string_index, cell_index + 1, bool_f, f_size)
        try:
            bool_f[string_index + 1][cell_index - 1] = bool_f[string_index + 1][cell_index - 1]
        except IndexError:
            pass
        else:
            if not bool_f[string_index + 1][cell_index - 1]:
                bool_f[string_index + 1][cell_index - 1] = True
                if field[string_index + 1][cell_index - 1] == ' 0 ':
                    open_around_zero(string_index + 1, cell_index - 1, bool_f, f_size)
        try:
            bool_f[string_index + 1][cell_index] = bool_f[string_index + 1][cell_index]
        except IndexError:
            pass
        else:
            if not bool_f[string_index + 1][cell_index]:
                bool_f[string_index + 1][cell_index] = True
                if field[string_index + 1][cell_index] == ' 0 ':
                    open_around_zero(string_index + 1, cell_index, bool_f, f_size)
        try:
            bool_f[string_index + 1][cell_index + 1] = bool_f[string_index + 1][cell_index + 1]
        except IndexError:
            pass
        else:
            if not bool_f[string_index + 1][cell_index + 1]:
                bool_f[string_index + 1][cell_index + 1] = True
                if field[string_index + 1][cell_index + 1] == ' 0 ':
                    open_around_zero(string_index + 1, cell_index + 1, bool_f, f_size)
    elif (string_index == 0) and (cell_index == 0):
        if not bool_f[string_index][cell_index + 1]:
            bool_f[string_index][cell_index + 1] = True
            if field[string_index][cell_index + 1] == ' 0 ':
                open_around_zero(string_index, cell_index + 1, bool_f, f_size)
        if not bool_f[string_index + 1][cell_index]:
            bool_f[string_index + 1][cell_index] = True
            if field[string_index + 1][cell_index] == ' 0 ':
                open_around_zero(string_index + 1, cell_index, bool_f, f_size)
        if not bool_f[string_index + 1][cell_index + 1]:
            bool_f[string_index + 1][cell_index + 1] = True
            if field[string_index + 1][cell_index + 1] == ' 0 ':
                open_around_zero(string_index + 1, cell_index + 1, bool_f, f_size)
    elif string_index == 0:
        if not bool_f[string_index][cell_index - 1]:
            bool_f[string_index][cell_index - 1] = True
            if field[string_index][cell_index - 1] == ' 0 ':
                open_around_zero(string_index, cell_index - 1, bool_f, f_size)
        if not bool_f[string_index + 1][cell_index - 1]:
            bool_f[string_index + 1][cell_index - 1] = True
            if field[string_index + 1][cell_index - 1] == ' 0 ':
                open_around_zero(string_index + 1, cell_index - 1, bool_f, f_size)
        if not bool_f[string_index + 1][cell_index]:
            bool_f[string_index + 1][cell_index] = True
            if field[string_index + 1][cell_index] == ' 0 ':
                open_around_zero(string_index + 1, cell_index, bool_f, f_size)
        try:
            bool_f[string_index + 1][cell_index + 1] = bool_f[string_index + 1][cell_index + 1]
        except IndexError:
            pass
        else:
            if not bool_f[string_index + 1][cell_index + 1]:
                bool_f[string_index + 1][cell_index + 1] = True
                if field[string_index + 1][cell_index + 1] == ' 0 ':
                    open_around_zero(string_index + 1, cell_index + 1, bool_f, f_size)
        try:
            bool_f[string_index][cell_index + 1] = bool_f[string_index][cell_index + 1]
        except IndexError:
            pass
        else:
            if not bool_f[string_index][cell_index + 1]:
                bool_f[string_index][cell_index + 1] = True
                if field[string_index][cell_index + 1] == ' 0 ':
                    open_around_zero(string_index, cell_index + 1, bool_f, f_size)
    elif cell_index == 0:
        if not bool_f[string_index - 1][cell_index]:
            bool_f[string_index - 1][cell_index] = True
            if field[string_index - 1][cell_index] == ' 0 ':
                open_around_zero(string_index - 1, cell_index, bool_f, f_size)
        if not bool_f[string_index - 1][cell_index + 1]:
            bool_f[string_index - 1][cell_index + 1] = True
            if field[string_index - 1][cell_index + 1] == ' 0 ':
                open_around_zero(string_index - 1, cell_index + 1, bool_f, f_size)
        if not bool_f[string_index - 1][cell_index + 1]:
            bool_f[string_index][cell_index + 1] = True
            if field[string_index][cell_index + 1] == ' 0 ':
                open_around_zero(string_index, cell_index + 1, bool_f, f_size)
        try:
            bool_f[string_index + 1][cell_index] = bool_f[string_index + 1][cell_index]
        except IndexError:
            pass
        else:
            if not bool_f[string_index + 1][cell_index]:
                bool_f[string_index + 1][cell_index] = True
                if field[string_index + 1][cell_index] == ' 0 ':
                    open_around_zero(string_index + 1, cell_index, bool_f, f_size)
        try:
            bool_f[string_index + 1][cell_index + 1] = bool_f[string_index + 1][cell_index + 1]
        except IndexError:
            pass
        else:
            if not bool_f[string_index + 1][cell_index + 1]:
                bool_f[string_index + 1][cell_index + 1] = True
                if field[string_index + 1][cell_index + 1] == ' 0 ':
                    open_around_zero(string_index + 1, cell_index + 1, bool_f, f_size)
    return bool_f


clear()
# Пользователь вводит размер поля
while True:
    while True:
        try:
            field_size = int(input('Введите размер поля: '))
        except ValueError:
            print('Ошибка! Введите число')
        else:
            break

    if (field_size >= 100) or (field_size <= 1):
        clear()
        print('Ошибка! Размер поля должен быть больше 1  и не больше 99')
        continue
    else:
        break

# Пользователь вводит количество бомб
while True:
    while True:
        try:
            bomb_quantity = int(input('Введите количество бомб: '))
        except ValueError:
            print('Ошибка! Введите число')
        else:
            break

    if (bomb_quantity >= field_size ** 2) or (bomb_quantity < 1):
        clear()
        print('Ошибка! Такое количество бомб не поддерживается полем')
        continue
    else:
        break

# Инициализация поля(field) и маски скрытия для поля(bool_field) и списка с бомбами(bomb_list)
bool_field = [[False] * field_size for i in range(field_size)]
field = [[' 0 '] * field_size for i in range(field_size)]
bomb_list = []

# Основной игровой цикл
first_select = True
game_over_flag = False
while not game_over_flag:
    clear()
    print('Для выхода из игры введите "end"')
    print_field(field, bool_field, field_size)
    # Прининимаем координаты ячейки от пользователя
    # Если пользователь ввёл 'end', то выходим из игры

    # Номер строки
    while True:
        user_select_x = input('Введите номер строки для выбора ячейки: ')
        if user_select_x == 'end':
            game_over_flag = True
            break
        try:
            user_select_x = int(user_select_x)
        except ValueError:
            clear()
            print('Для выхода из игры введите "end"')
            print_field(field, bool_field, field_size)
            print('Ошибка! Введите число!')
            continue
        if (user_select_x < 1) or (user_select_x > field_size):
            clear()
            print('Для выхода из игры введите "end"')
            print_field(field, bool_field, field_size)
            print(f'Ошибка! Значение должно быть от 1 до {field_size}')
            continue
        else:
            break
    if game_over_flag:
        break

    clear()
    print('Для выхода из игры введите "end"')
    print_field(field, bool_field, field_size)
    # Номер столбца
    while True:
        user_select_y = input('Введите номер столбца для выбора ячейки: ')
        if user_select_y == 'end':
            game_over_flag = True
            break
        try:
            user_select_y = int(user_select_y)
        except ValueError:
            clear()
            print('Для выхода из игры введите "end"')
            print_field(field, bool_field, field_size)
            print('Ошибка! Введите число!')
            continue
        if (user_select_y < 1) or (user_select_y > field_size):
            clear()
            print('Для выхода из игры введите "end"')
            print_field(field, bool_field, field_size)
            print(f'Ошибка! Значение должно быть от 1 до {field_size}')
            continue
        else:
            break
    if game_over_flag:
        break

    # При первом выборе ячеки пользователя(first_selection == true), инициализируем поле
    # То есть создаём бомбы(' * ')
    # В других клетках счётчик кол-ва бомб в соседних ячейках
    if first_select:
        # Открываем первую ячейку, выбранную пользователем
        # Инициализируем рандомно бомбы по остальному списку
        bool_field[user_select_x - 1][user_select_y - 1] = True
        for item in range(bomb_quantity):
            while True:
                bomb_list.append([random.randint(0, field_size - 1), random.randint(0, field_size - 1)])
                if bomb_list[-1] == [user_select_x - 1, user_select_y - 1]:
                    bomb_list.pop()
                else:
                    break
        for bomb in bomb_list:
            field[bomb[0]][bomb[1]] = ' * '

        count_string = 0
        # Для ячеек без бомб подсчитываем кол-во соседних ячеек с бомбами
        for string in field:
            count_cell = 0
            for item in string:
                if item != ' * ':
                    count_bomb = 0
                    if (count_string != 0) and (count_cell != 0) and (count_string != field_size - 1) and (
                            count_cell != field_size - 1):
                        if field[count_string][count_cell - 1] == ' * ':
                            count_bomb += 1
                        if field[count_string][count_cell + 1] == ' * ':
                            count_bomb += 1
                        if field[count_string - 1][count_cell - 1] == ' * ':
                            count_bomb += 1
                        if field[count_string - 1][count_cell] == ' * ':
                            count_bomb += 1
                        if field[count_string - 1][count_cell + 1] == ' * ':
                            count_bomb += 1
                        if field[count_string + 1][count_cell - 1] == ' * ':
                            count_bomb += 1
                        if field[count_string + 1][count_cell] == ' * ':
                            count_bomb += 1
                        if field[count_string + 1][count_cell + 1] == ' * ':
                            count_bomb += 1
                    elif (count_string == 0) and (count_cell != 0) and (count_cell != field_size - 1):
                        if field[count_string][count_cell - 1] == ' * ':
                            count_bomb += 1
                        if field[count_string][count_cell + 1] == ' * ':
                            count_bomb += 1
                        if field[count_string + 1][count_cell - 1] == ' * ':
                            count_bomb += 1
                        if field[count_string + 1][count_cell] == ' * ':
                            count_bomb += 1
                        if field[count_string + 1][count_cell + 1] == ' * ':
                            count_bomb += 1
                    elif (count_string == field_size - 1) and (count_cell != 0) and (count_cell != field_size - 1):
                        if field[count_string][count_cell - 1] == ' * ':
                            count_bomb += 1
                        if field[count_string][count_cell + 1] == ' * ':
                            count_bomb += 1
                        if field[count_string - 1][count_cell - 1] == ' * ':
                            count_bomb += 1
                        if field[count_string - 1][count_cell] == ' * ':
                            count_bomb += 1
                        if field[count_string - 1][count_cell + 1] == ' * ':
                            count_bomb += 1
                    elif (count_cell == 0) and (count_string != 0) and (count_string != field_size - 1):
                        if field[count_string][count_cell + 1] == ' * ':
                            count_bomb += 1
                        if field[count_string - 1][count_cell] == ' * ':
                            count_bomb += 1
                        if field[count_string - 1][count_cell + 1] == ' * ':
                            count_bomb += 1
                        if field[count_string + 1][count_cell] == ' * ':
                            count_bomb += 1
                        if field[count_string + 1][count_cell + 1] == ' * ':
                            count_bomb += 1
                    elif (count_cell == field_size - 1) and (count_string != 0) and (count_string != field_size - 1):
                        if field[count_string][count_cell - 1] == ' * ':
                            count_bomb += 1
                        if field[count_string - 1][count_cell - 1] == ' * ':
                            count_bomb += 1
                        if field[count_string - 1][count_cell] == ' * ':
                            count_bomb += 1
                        if field[count_string + 1][count_cell - 1] == ' * ':
                            count_bomb += 1
                        if field[count_string + 1][count_cell] == ' * ':
                            count_bomb += 1
                    elif (count_string == 0) and (count_cell == 0):
                        if field[count_string][count_cell + 1] == ' * ':
                            count_bomb += 1
                        if field[count_string + 1][count_cell] == ' * ':
                            count_bomb += 1
                        if field[count_string + 1][count_cell + 1] == ' * ':
                            count_bomb += 1
                    elif (count_string == 0) and (count_cell == field_size - 1):
                        if field[count_string][count_cell - 1] == ' * ':
                            count_bomb += 1
                        if field[count_string + 1][count_cell - 1] == ' * ':
                            count_bomb += 1
                        if field[count_string + 1][count_cell] == ' * ':
                            count_bomb += 1
                    elif (count_string == field_size - 1) and (count_cell == 0):
                        if field[count_string][count_cell + 1] == ' * ':
                            count_bomb += 1
                        if field[count_string - 1][count_cell] == ' * ':
                            count_bomb += 1
                        if field[count_string - 1][count_cell + 1] == ' * ':
                            count_bomb += 1
                    elif (count_string == field_size - 1) and (count_cell == field_size - 1):
                        if field[count_string][count_cell - 1] == ' * ':
                            count_bomb += 1
                        if field[count_string - 1][count_cell - 1] == ' * ':
                            count_bomb += 1
                        if field[count_string - 1][count_cell] == ' * ':
                            count_bomb += 1
                    field[count_string][count_cell] = f' {count_bomb} '
                count_cell += 1
            count_string += 1
        if field[user_select_x - 1][user_select_y - 1] == ' 0 ':
            bool_field = open_around_zero(user_select_x - 1, user_select_y - 1, bool_field, field_size)
        first_select = False

    # Открываем ячейки, выбранные пользователем
    else:
        bool_field[user_select_x - 1][user_select_y - 1] = True
        if field[user_select_x - 1][user_select_y - 1] == ' * ':
            clear()
            print_field(field, bool_field, field_size)
            print('Game over! You lose!')
            game_over_flag = True
            break
        if field[user_select_x - 1][user_select_y - 1] == ' 0 ':
            bool_field = open_around_zero(user_select_x - 1, user_select_y - 1, bool_field, field_size)

    # Активируем флаг об окончании игры, если все ячейки без бомб открыты
    all_open = True
    count_string = 0
    for string in field:
        count_cell = 0
        for item in string:
            if (item != ' * ') and (not bool_field[count_string][count_cell]):
                all_open = False
            count_cell += 1
        count_string += 1

    if all_open:
        print('Game over! You win!')
        game_over_flag = True

for string in field:
    print(string)
