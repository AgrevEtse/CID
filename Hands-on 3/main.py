from DataSet import DataSet
from DiscreteMaths import DiscreteMaths
from SLR import SLR
from QR import QR
from CR import CR

# Object Instances
data_set = DataSet()
discrete_maths = DiscreteMaths(data_set.get_n())
slr = SLR()
qr = QR()
cr = CR()

# SLR Operations and prints
def slr_operations():
    # Calulating beta_1 and beta_0
    slr.to_compute_beta_1(discrete_maths.sum_xy(data_set.get_x(), data_set.get_y()), discrete_maths.sum_x_sum_y(data_set.get_x(), data_set.get_y()), discrete_maths.sum_x_quad(data_set.get_x()), discrete_maths.sum_x_sum_x(data_set.get_x()), data_set.get_n())

    slr.to_compute_beta_0(discrete_maths.sum_y(data_set.get_y()), discrete_maths.sum_x(data_set.get_x()), data_set.get_n())

    # Print of the regression equation
    slr.to_print_regression_eq()

    # Predictions
    print('\nPredictions')
    slr.print_prediction(62)
    slr.print_prediction(67) # Value from the dataset
    slr.print_prediction(77)
    slr.print_prediction(83) # Value from the dataset

    print('\nCoefficients')

    # Coefficient of Determination
    slr.to_compute_coefficient_determination(data_set.get_x(), data_set.get_y(), data_set.get_n())
    print(f'R^2 / Determination = {slr.get_coefficient_determination()}')

    # Coefficient of Correlation
    slr.to_compute_coefficient_correlation()
    print(f'R   / Correlation   = {slr.get_coefficient_correlation()}')

# QR Operations and prints
def qr_operations():
    qr.to_compute_equation(data_set.get_n(), discrete_maths.sum_x(data_set.get_x()), discrete_maths.sum_x_quad(data_set.get_x()), discrete_maths.sum_x_cub(data_set.get_x()), discrete_maths.sum_x_fourth(data_set.get_x()), discrete_maths.sum_y(data_set.get_y()), discrete_maths.sum_xy(data_set.get_x(), data_set.get_y()), discrete_maths.sum_x_quad_y(data_set.get_x(), data_set.get_y()))

    qr.to_print_regression_eq()

    print('\nPredictions')
    qr.print_prediction(62)
    qr.print_prediction(67) # Value from the dataset
    qr.print_prediction(77)
    qr.print_prediction(83) # Value from the dataset

    print('\nCoefficients')
    qr.to_compute_coefficient_determination(data_set.get_x(), data_set.get_y(), data_set.get_n())
    print(f'R^2 / Determination = {qr.get_coefficient_determination()}')

    qr.to_compute_coefficient_correlation()
    print(f'R   / Correlation   = {qr.get_coefficient_correlation()}')

# CR Operations and prints
def cr_operations():
    cr.to_compute_equation(data_set.get_n(), discrete_maths.sum_x(data_set.get_x()), discrete_maths.sum_x_quad(data_set.get_x()), discrete_maths.sum_x_cub(data_set.get_x()), discrete_maths.sum_x_fourth(data_set.get_x()), discrete_maths.sum_x_fifth(data_set.get_x()), discrete_maths.sum_x_sixth(data_set.get_x()), discrete_maths.sum_y(data_set.get_y()), discrete_maths.sum_xy(data_set.get_x(), data_set.get_y()), discrete_maths.sum_x_quad_y(data_set.get_x(), data_set.get_y()), discrete_maths.sum_x_cub_y(data_set.get_x(), data_set.get_y()))

    cr.to_print_regression_eq()

    print('\nPredictions')
    cr.print_prediction(62)
    cr.print_prediction(67) # Value from the dataset
    cr.print_prediction(77)
    cr.print_prediction(83) # Value from the dataset

    print('\nCoefficients')

    cr.to_compute_coefficient_determination(data_set.get_x(), data_set.get_y(), data_set.get_n())
    print(f'R^2 / Determination = {cr.get_coefficient_determination()}')

    cr.to_compute_coefficient_correlation()
    print(f'R   / Correlation   = {cr.get_coefficient_correlation()}')

# Main Function
def main():
    print(f'{'-' * 50} LR {'-' * 50}')
    slr_operations()
    print(f'{'-' * 50} QR {'-' * 50}')
    qr_operations()
    print(f'{'-' * 50} CR {'-' * 50}')
    cr_operations()
    print(f'{'-' * 104}')

if __name__ == "__main__":
    main()