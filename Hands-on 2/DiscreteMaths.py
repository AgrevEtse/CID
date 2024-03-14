from typing import List

class DiscreteMaths:
    def __init__(self, n: int):
        self.__private_n: int = n

    # Summation of X's Values
    def sum_x(self, data: List[float]) -> float:
        total = 0.0
        for i in range(self.__private_n):
            total += data[i]

        return total

    # Summation of Y's Values
    def sum_y(self, data: List[float]) -> float:
        total = 0.0
        for i in range(self.__private_n):
            total += data[i]

        return total

    # Summation of X's Values Squared
    def sum_x_quad(self, data: List[float]) -> float:
        total = 0.0
        for i in range(self.__private_n):
            total += data[i] * data[i]

        return total

    # Summation of Y's Values Squared
    def sum_y_quad(self, data: List[float]) -> float:
        total = 0.0
        for i in range(self.__private_n):
            total += data[i] * data[i]

        return total

    # Summation of X's Values Times Y's Values
    def sum_xy(self, data_x: List[float], data_y: List[float]) -> float:
        total = 0.0
        for i in range(self.__private_n):
            total += data_x[i] * data_y[i]

        return total

    # Summation of X's Values Times Summation of X's Values
    def sum_x_sum_x(self, data: List[float]) -> float:
        return self.sum_x(data) * self.sum_x(data)

    # Summation of Y's Values Times Summation of Y's Values
    def sum_y_sum_y(self, data: List[float]) -> float:
        return self.sum_y(data) * self.sum_y(data)

    # Summation of X's Values Times Summation of Y's Values
    def sum_x_sum_y(self, data_x: List[float], data_y: List[float]) -> float:
        return self.sum_x(data_x) * self.sum_y(data_y)