class DiscreteMaths:
    def __init__(self, n: int):
        self.__private_n: int = n

    # Summation of X's Values
    def sum_x(self, data: list[float]) -> float:
        total = 0.0
        for i in range(self.__private_n):
            total += data[i]

        return total

    # Summation of Y's Values
    def sum_y(self, data: list[float]) -> float:
        total = 0.0
        for i in range(self.__private_n):
            total += data[i]

        return total

    # Summation of X's Values ^ 2
    def sum_x_quad(self, data: list[float]) -> float:
        total = 0.0
        for i in range(self.__private_n):
            total += data[i] ** 2

        return total

    # Summation of X's Values ^ 3
    def sum_x_cub(self, data: list[float]) -> float:
        total = 0.0
        for i in range(self.__private_n):
            total += data[i] ** 3

        return total

    # Summation of X's Values ^ 4
    def sum_x_fourth(self, data: list[float]) -> float:
        total = 0.0
        for i in range(self.__private_n):
            total += data[i] ** 4

        return total

    # Summation of X's Values ^ 5
    def sum_x_fifth(self, data: list[float]) -> float:
        total = 0.0
        for i in range(self.__private_n):
            total += data[i] ** 5

        return total

    # Summation of X's Values ^ 6
    def sum_x_sixth(self, data: list[float]) -> float:
        total = 0.0
        for i in range(self.__private_n):
            total += data[i] ** 6

        return total

    # Summation of Y's Values Squared
    def sum_y_quad(self, data: list[float]) -> float:
        total = 0.0
        for i in range(self.__private_n):
            total += data[i] * data[i]

        return total

    # Summation of X's Values Times Y's Values
    def sum_xy(self, data_x: list[float], data_y: list[float]) -> float:
        total = 0.0
        for i in range(self.__private_n):
            total += data_x[i] * data_y[i]

        return total

    def sum_x_quad_y(self, data_x: list[float], data_y: list[float]) -> float:
        total = 0.0
        for i in range(self.__private_n):
            total += (data_x[i] ** 2) * data_y[i]

        return total

    def sum_x_cub_y(self, data_x: list[float], data_y: list[float]) -> float:
        total = 0.0
        for i in range(self.__private_n):
            total += (data_x[i] ** 3) * data_y[i]

        return total

    # Summation of X's Values Times Summation of X's Values
    def sum_x_sum_x(self, data: list[float]) -> float:
        return self.sum_x(data) * self.sum_x(data)

    # Summation of Y's Values Times Summation of Y's Values
    def sum_y_sum_y(self, data: list[float]) -> float:
        return self.sum_y(data) * self.sum_y(data)

    # Summation of X's Values Times Summation of Y's Values
    def sum_x_sum_y(self, data_x: list[float], data_y: list[float]) -> float:
        return self.sum_x(data_x) * self.sum_y(data_y)