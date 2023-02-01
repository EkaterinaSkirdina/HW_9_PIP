# Задача 3. Создайте программу для игры в ""Крестики-нолики"" 
# при помощи виртуального окружения и PIP

# Решение:

def print_maps():                 # Функция печати игрового поля
    print(maps[0], end = " ")
    print(maps[1], end = " ")
    print(maps[2])
 
    print(maps[3], end = " ")
    print(maps[4], end = " ")
    print(maps[5])
 
    print(maps[6], end = " ")
    print(maps[7], end = " ")
    print(maps[8])

def step_maps(step, symbol):      # Функция хода
    i = maps.index(step)
    maps[i] = symbol

def get_result():                 # Проверка победителя
    win = ''
    for i in victories:
        if maps[i[0]] == 'X' and maps[i[1]] == 'X' and maps[i[2]] == 'X':
            win = 'X'
        if maps[i[0]] == '0' and maps[i[1]] == '0' and maps[i[2]] == '0':
            win = '0'
    return win

maps = [1, 2, 3,         # Игровое поле
        4, 5, 6,
        7, 8, 9]

victories = [[0,1,2],    # Выигрышные комбинации
             [3,4,5],
             [6,7,8],
             [0,3,6],
             [1,4,7],
             [2,5,8],
             [0,4,8],
             [2,4,6]]

finish = False
player1 = True
count = 0          # Счетчик ходов, на случай ничьей
print_maps()
while finish == False and count < 9:
    if player1 == True:
        symbol = 'X'
        step = int(input("Ходит 'X': "))
    else:
        symbol = '0'
        step = int(input("Ходит '0': "))
    if step not in maps:
        step = int(input('Вы ввели не верное значение, попробуйте снова: '))
    step_maps(step, symbol)
    print_maps()
    win = get_result()
    if win != '':
        finish = True
        print('Игра окончена! Победил', win, '!!!')
        break
    else:
        player1 = not player1
        count += 1
else:
    print('Игра окончена. Победила дружба!!!')