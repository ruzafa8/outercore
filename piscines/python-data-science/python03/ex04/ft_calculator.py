class calculator:
    """Class for doing cals with lists"""

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Makes the dot product of two vectors"""
        res = [float(V1[i]) * float(V2[i]) for i in range(len(V1))]
        print(sum(res))

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Sum elements of each array by position"""
        res = [float(V1[i]) + float(V2[i]) for i in range(len(V1))]
        print(res)

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Subtracts elements of each array by position"""
        res = [float(V1[i]) - float(V2[i]) for i in range(len(V1))]
        print(res)
