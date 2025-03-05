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
