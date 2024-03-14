from typing import List
import numpy as np

class SLR:
    def __init__(self):
        self.__private_beta_0: float = 0.0
        self.__private_beta_1: float = 0.0
        self.__private_coefficient_determination: float = 0.0
        self.__private_coefficient_correlation: float = 0.0

    # Getters
    def get_coefficient_determination(self) -> float:
        return self.__private_coefficient_determination

    def get_coefficient_correlation(self) -> float:
        return self.__private_coefficient_correlation

    # beta_0 = (sum(y) - beta_1 * sum(x)) / n
    def to_compute_beta_0(self, sum_y: float, sum_x: float, n: int) -> None:
        self.__private_beta_0 = (sum_y - (self.__private_beta_1 * sum_x)) / n

    # beta_1 = (n * sum(xy) - sum(x) * sum(y)) / (n * sum(x^2) - sum(x)^2)
    def to_compute_beta_1(self, sum_xy: float, sum_x_sum_y: float, sum_x_quad: float, sum_x_sum_x: float, n: int) -> None:
        self.__private_beta_1 = ((n * sum_xy) - sum_x_sum_y) / ((n * sum_x_quad) - sum_x_sum_x)

    # Coefficient of Determination / R^2 = 1 - (SSR / SST)
    # SSR = Residual Sum of Square (sum (y - y^) ^ 2)
    # SST = Total Sum of Square (sum (y - y_avg) ^ 2)
    def to_compute_coefficient_determination(self, data_x: List[float], data_y: List[float], n: int) -> None:
        avg = 0
        ssr = 0
        sst = 0

        # Average
        for i in range(n):
            avg += data_y[i]
        avg /= n

        # SSR
        for i in range(n):
            ssr += ((data_y[i] - self.to_predict(data_x[i])) ** 2)

        # SST
        for i in range(n):
            sst += ((data_y[i] - avg) ** 2)

        self.__private_coefficient_determination = round(1 - (ssr / sst), 4)

    # Coefficient of Correlation / R = sqrt(R^2)
    def to_compute_coefficient_correlation(self) -> None:
        self.__private_coefficient_correlation = round(np.sqrt(self.__private_coefficient_determination), 4)

    # Print of the regression equation using the computed beta_0 and beta_1
    def to_print_regression_eq(self) -> None:
        print(f'Simple Linear Regression Equation\nY = {round(self.__private_beta_0, 2)} + {round(self.__private_beta_1, 2)}x')

    # Prediction of a value using the regression equation
    def to_predict(self, independent_var: float) -> float:
        return round(self.__private_beta_0 + (self.__private_beta_1 * independent_var), 2)

    # Print of the prediction of a value using the regression equation
    def print_prediction(self, independent_var: float) -> None:
        print(f'X = {independent_var}, Y = {round(self.to_predict(independent_var), 2)}')