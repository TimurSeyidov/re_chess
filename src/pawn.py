from .colors import BlackColor, WhiteColor


class Pawn:
    def __init__(self,
                 color: BlackColor | WhiteColor
                 ):
        self.__color = color

    @property
    def char(self) -> str:
        if self.__color.is_white():
            return 'wP'
        return 'bP'

    def can_move(self,
                 board,
                 from_row: int,
                 from_col: int,
                 to_row: int,
                 to_col: int
                 ) -> bool:
        pass
