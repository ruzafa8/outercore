class calculator:
    def __init__(self, arr):
        self.arr = arr

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        res = []
        for i in range(len(V1)):
            res.append(float(V1[i]) * float(V2[i]))
        print(sum(res))

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        res = []
        for i in range(len(V1)):
            res.append(float(V1[i]) + float(V2[i]))
        print(res)

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        res = []
        for i in range(len(V1)):
            res.append(float(V1[i]) - float(V2[i]))
        print(res)
