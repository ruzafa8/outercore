class calculator:
    """Class for doing cals for each element of a list"""
    def __init__(self, arr):
        """Calculator class receives an initial array
        where to apply the operations.
        Be carrefour, you cannot change the size later."""
        self.arr = arr

    def __add__(self, object) -> None:
        """Applies a sum to each element"""
        self.arr = list(map(lambda x: x + object, self.arr))
        print(self.arr)

    def __mul__(self, object) -> None:
        """Applies a mul to each element"""
        self.arr = list(map(lambda x: x * object, self.arr))
        print(self.arr)

    def __sub__(self, object) -> None:
        """Applies a sub to each element"""
        self.arr = list(map(lambda x: x - object, self.arr))
        print(self.arr)

    def __truediv__(self, object) -> None:
        """Applies a decimal div to each element"""
        if object == 0:
            raise ZeroDivisionError()
        self.arr = list(map(lambda x: x // object, self.arr))
        print(self.arr)
