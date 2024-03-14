from typing import List

class DataSet:
    def __init__(self):
        # Hardcoded data
        self.__private_x: List[float] = [108.0, 115.0, 106.0, 97.0, 95.0, 91.0, 97.0, 83.0, 83.0, 78.0, 54.0, 67.0, 56.0, 53.0, 61.0, 115.0, 81.0, 78.0, 30.0, 45.0, 99.0, 32.0, 25.0, 28.0, 90.0, 89.0]

        self.__private_y: List[float] = [95.0, 96.0, 95.0, 97.0, 93.0, 94.0, 95.0, 93.0, 92.0, 86.0, 73.0, 80.0, 65.0, 69.0, 77.0, 96.0, 87.0, 89.0, 60.0, 63.0, 95.0, 61.0, 55.0, 56.0, 94.0, 93.0]
        self.__private_n: int = len(self.__private_x)

    # Getters
    def get_x(self) -> List[float]:
        return self.__private_x

    def get_y(self) -> List[float]:
        return self.__private_y

    def get_n(self) -> List[float]:
        return self.__private_n