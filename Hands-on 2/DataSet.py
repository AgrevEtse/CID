class DataSet:
    def __init__(self):
        # Hardcoded data
        self.__private_x: list[float] = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]
        self.__private_y: list[float] = [5.0, 10.0, 15.0, 20.0, 25.0, 30.0, 35.0, 40.0, 45.0]
        self.__private_n: int = len(self.__private_x)

    # Getters
    def get_x(self) -> list[float]:
        return self.__private_x

    def get_y(self) -> list[float]:
        return self.__private_y

    def get_n(self) -> int:
        return self.__private_n