class Binary(bytes):
    def __new__(cls, val):
        return super().__new__(cls, val)

class Boolean(bool):
    def __new__(cls, val):
        return super().__new__(cls, val)


class Integer(int):
    def __new__(cls, val):
        return super().__new__(cls, val)


class Number(float):
    def __new__(cls, val):
        return super().__new__(cls, val)


class String(str):
    def __new__(cls, val):
        return super().__new__(cls, val)
