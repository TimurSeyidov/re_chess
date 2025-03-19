from .figure import Figure


class Pawn(Figure):
    @property
    def char(self) -> str:
        if self.color.is_white():
            return 'wP'
        return 'bP'

    def can_move(self,
                 board,
                 from_row: int,
                 from_col: int,
                 to_row: int,
                 to_col: int
                 ) -> bool:
        if from_col != to_col:
            return False
        if self.color.is_white():
            direction = 1
        else:
            direction = -1
        accepted_rows = [from_row + direction]
        if self.color.is_white() and from_row == 1 or self.color.is_black() and from_row == 6:
            accepted_rows.append(from_row + direction * 2)
        return to_row in accepted_rows

    def can_attack(self,
                 board,
                 from_row: int,
                 from_col: int,
                 to_row: int,
                 to_col: int
                 ) -> bool:
        if abs(from_col - to_col) != 1:
            return False
        if self.color.is_white():
            direction = 1
        else:
            direction = -1
        return to_row - from_row == direction
