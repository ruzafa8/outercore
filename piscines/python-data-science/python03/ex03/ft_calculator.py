class calculator:
    def __init__(self, arr):
        self.arr = arr

    def __add__(self, object) -> None:
        self.arr = list(map(lambda x: x + object, self.arr))
        print(self.arr)

    def __mul__(self, object) -> None:
        self.arr = list(map(lambda x: x * object, self.arr))
        print(self.arr)

    def __sub__(self, object) -> None:
        self.arr = list(map(lambda x: x - object, self.arr))
        print(self.arr)

    def __truediv__(self, object) -> None:
        if object == 0:
            raise ZeroDivisionError()
        self.arr = list(map(lambda x: x // object, self.arr))
        print(self.arr)
