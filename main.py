import re
from src.board import Board


def print_board(board: Board):
    print('  +' + '----+' * 8)
    for row in range(8, 0, -1):
        print(str(row) + ' |', end='')
        for col in range(8):
            print(' ', end='')
            player = board.get_item(row - 1, col)
            if player:
                print(player.char, end='')
            else:
                print('  ', end='')
            print(' |', end='')
        print()
        print('  +' + '----+' * 8)
    print('   ', end='')
    ix = ord('A')
    for col in range(8):
        print(f' {chr(ix + col)}   ', end='')
    print()

def print_menu():
    print('exit                       - Выход')
    print('move <col><row> <col><row> - движение фигуры')


_board = Board()
pattern = r'^move ([A-H]{1}[1-8]{1}) ([A-H]{1}[1-8]{1})$'
while True:
    print_board(_board)
    print()
    print('Ходят', end=' ')
    print()
    if _board.color.is_white():
        print('белые')
    else:
        print('черные')
    print_menu()
    cmd = input('Введите команду: ').strip()
    try:
        if cmd == 'exit':
            break
        match = re.match(pattern, cmd)
        if match is None:
            raise Exception('Неверная команда')
        start = _board.convert(match.group(1))
        end = _board.convert(match.group(2))
        if not start or not end:
            raise Exception('Неверные координаты')

    except Exception as e:
        print(e)
        input('Нажмите любую клавишу для продолжения...')
