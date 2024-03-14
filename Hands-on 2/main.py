from DataSet import DataSet
from DiscreteMaths import DiscreteMaths
from SLR import SLR

# Main Function
def main():
    # Object Instances
    data_set = DataSet()
    discrete_maths = DiscreteMaths(data_set.get_n())
    slr = SLR()

    # Calulating beta_1 and beta_0
    slr.to_compute_beta_1(discrete_maths.sum_xy(data_set.get_x(), data_set.get_y()), discrete_maths.sum_x_sum_y(data_set.get_x(), data_set.get_y()), discrete_maths.sum_x_quad(data_set.get_x()), discrete_maths.sum_x_sum_x(data_set.get_x()), data_set.get_n())

    slr.to_compute_beta_0(discrete_maths.sum_y(data_set.get_y()), discrete_maths.sum_x(data_set.get_x()), data_set.get_n())

    # Print of the regression equation
    slr.to_print_regression_eq()

    # Prediction using the regression equation
    print(f'X = 60, Y = {slr.to_predict(60)}\n')

    # Coefficient of Correlation
    slr.to_compute_coefficient_correlation(data_set.get_x(), data_set.get_y(), data_set.get_n())
    print(f'Coefficient of correlation: {slr.get_coefficient_correlation()}')

    # Coefficient of Determination
    slr.to_compute_coefficient_determination()
    print(f'Coefficient of determination: {slr.get_coefficient_determination()}\n')

    # Predictions
    print('Predictions:')
    slr.print_prediction(65)
    slr.print_prediction(71)
    slr.print_prediction(77)
    slr.print_prediction(84)
    slr.print_prediction(89)

if __name__ == "__main__":
    main()