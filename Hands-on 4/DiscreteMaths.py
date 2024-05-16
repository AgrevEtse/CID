class DiscreteMaths:
    def __init__(self, n: int) -> None:
        self.__private_n = n

    # Euclidean Distance
    def euclidean_distance(self, x1: list[float], x2: list[float]) -> float:
        distance = 0
        for i in range(self.__private_n):
            distance += (x1[i] - x2[i]) ** 2
        return distance ** 0.5

    # Manhattan Distance
    def manhattan_distance(self, x1: list[float], x2: list[float]) -> float:
        distance = 0
        for i in range(self.__private_n):
            distance += abs(x1[i] - x2[i])
        return distance