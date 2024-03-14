from typing import List

class DataSet:
    def __init__(self):
        # Hardcoded data
        self.__private_x: List[float] = [23.0, 26.0, 30.0, 34.0, 43.0, 48.0, 52.0, 57.0, 58.0]
        self.__private_y: List[float] = [651.0, 762.0, 856.0, 1063.0, 1190.0, 1298.0, 1421.0, 1440.0, 1518.0]
        self.__private_n: int = len(self.__private_x)

    # Getters
    def get_x(self) -> List[float]:
        return self.__private_x

    def get_y(self) -> List[float]:
        return self.__private_y

    def get_n(self) -> List[float]:
        return self.__private_n