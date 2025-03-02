class BlackColor:
    @staticmethod
    def is_white() -> bool:
        return False

    @staticmethod
    def is_black() -> bool:
        return True

    @staticmethod
    def get_opponent():
        return WhiteColor

class WhiteColor:
    @staticmethod
    def is_white() -> bool:
        return True

    @staticmethod
    def is_black() -> bool:
        return False

    @staticmethod
    def get_opponent():
        return BlackColor

class Board:
    def __init__(self):
        self.__board = []
        for _ in range(8):
            self.__board.append([None] * 8)


def print_board(board: Board):
    print('  +' + '----+' * 8)
    for row in range(8, 0, -1):
        print(str(row) + ' |', end='')
        for col in range(8):
            print('    |', end='')
        print()
        print('  +' + '----+' * 8)
    print('   ', end='')
    ix = ord('A')
    for col in range(8):
        print(f' {chr(ix + col)}   ', end='')
    print()


board = Board()
print_board(board)