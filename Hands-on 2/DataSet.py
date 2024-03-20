from typing import List

class DataSet:
    def __init__(self):
        # Hardcoded data
        self.__private_x: List[float] = [1,2,3,4,5,6,7,8,9]
        self.__private_y: List[float] = [5,10,15,20,25,30,35,40,45]
        self.__private_n: int = len(self.__private_x)

    # Getters
    def get_x(self) -> List[float]:
        return self.__private_x

    def get_y(self) -> List[float]:
        return self.__private_y

    def get_n(self) -> List[float]:
        return self.__private_n