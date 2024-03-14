from typing import List
import numpy as np

class CR:
    def __init__(self):
        self.__private_a_0: float = 0.0
        self.__private_a_1: float = 0.0
        self.__private_a_2: float = 0.0
        self.__private_a_3: float = 0.0
        self.__private_coefficient_determination: float = 0.0
        self.__private_coefficient_correlation: float = 0.0

    # Getters
    def get_coefficient_determination(self) -> float:
        return self.__private_coefficient_determination

    def get_coefficient_correlation(self) -> float:
        return self.__private_coefficient_correlation

    # [ [n, sum_x, sum_x_quad, sum_x_cub],
    #   [sum_x, sum_x_quad, sum_x_cub, sum_x_fourth],
    #   [sum_x_quad, sum_x_cub, sum_x_fourth, sum_x_fifth],
    #   [sum_x_cub, sum_x_fourth, sum_x_fifth, sum_x_sixth] ] ^ -1
    # * [sum_y, sum_xy, sum_x_quad_y, sum_x_cub_y]
    # = [a0, a1, a2, a3]
    def to_compute_equation(self, n: int, sum_x: float, sum_x_quad: float, sum_x_cub: float, sum_x_fourth: float, sum_x_fifth: float, sum_x_sixth: float, sum_y: float, sum_xy: float, sum_x_quad_y: float, sum_x_cub_y: float) -> None:

        # X Matrix
        x_matrix = np.array([[n, sum_x, sum_x_quad, sum_x_cub], [sum_x, sum_x_quad, sum_x_cub, sum_x_fourth], [sum_x_quad, sum_x_cub, sum_x_fourth, sum_x_fifth], [sum_x_cub, sum_x_fourth, sum_x_fifth, sum_x_sixth]])

        # B Array
        b_array = np.array([sum_y, sum_xy, sum_x_quad_y, sum_x_cub_y])

        # Inverse of X Matrix * B Array
        results = np.dot(np.linalg.inv(x_matrix), b_array)

        self.__private_a_0 = round(results[0], 6)
        self.__private_a_1 = round(results[1], 6)
        self.__private_a_2 = round(results[2], 6)
        self.__private_a_3 = round(results[3], 6)

    # Coefficient of Correlation / R^2 = 1 - (SSE / SST)
    # SSE =  (sum (y - ax^2 - bx - c) ^ 2)
    # SST = Total Sum of Square (sum (y - y_avg) ^ 2)
    def to_compute_coefficient_correlation(self, data_x: List[float], data_y: List[float], n: int):
        avg = 0
        sse = 0
        sst = 0

        # Average
        for i in range(n):
            avg += data_y[i]
        avg /= n

        # SSE
        for i in range(n):
            sse += ((data_y[i] - self.to_predict(data_x[i])) ** 2)

        # SST
        for i in range(n):
            sst += ((data_y[i] - avg) ** 2)

        self.__private_coefficient_correlation = round(1 - (sse / sst), 4)

    # Coefficient of Determination / R = sqrt(R^2)
    def to_compute_coefficient_determination(self) -> None:
        self.__private_coefficient_determination = round(np.sqrt(self.__private_coefficient_correlation), 4)

    # Print of the regression equation using the computed a_0, a_1, a_2, and a_3
    def to_print_regression_eq(self) -> None:
        print(f'Cubic Regression Equation\nY = {self.__private_a_0} + {self.__private_a_1}x + {self.__private_a_2}x^2 + {self.__private_a_3}x^3')

    # Prediction of a value using the regression equation
    def to_predict(self, independent_var: float) -> float:
        return round(self.__private_a_0 + (self.__private_a_1 * independent_var) + (self.__private_a_2 * (independent_var ** 2)) + (self.__private_a_3 * (independent_var ** 3)), 2)

    # Print of the prediction of a value using the regression equation
    def print_prediction(self, independent_var: float) -> None:
        print(f'X = {independent_var}, Y = {self.to_predict(independent_var)}')