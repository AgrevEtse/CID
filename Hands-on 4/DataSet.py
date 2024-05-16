class DataSet:
    # Hardcoded data
    def __init__(self):
        # [Height (cms), Weight (kgs)]
        self.__private_x: list[list[float, float]] = [[158, 58], [158, 59], [158, 63], [160, 59], [160, 60], [163, 60], [163, 61], [160, 64], [163, 64], [165, 61], [165, 62], [165, 65], [168, 62], [168, 63], [168, 66], [170, 63], [170, 64], [170, 68]]

        # T-Shirt Size: 0 = Medium, 1 = Large
        self.__private_y: list[float] = [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        self.__private_n: int = len(self.__private_x)

    # Getters
    def get_x(self) -> list[float]:
        return self.__private_x

    def get_y(self) -> list[float]:
        return self.__private_y

    def get_n(self) -> int:
        return self.__private_n