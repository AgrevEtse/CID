from DataSet import DataSet
from KNNClassifier import KNNClassifier

# Main function
def main() -> None:
    # Object Instances
    ds = DataSet()
    knn = KNNClassifier(metric = 'euclidean')

    # Training data
    knn.fit(ds.get_x(), ds.get_y())

    # Test data
    X_test = [[160, 163], [158, 60], [156, 56], [159, 55], [169, 70]] # [Height (cms), Weight (kgs)]
    predictions = knn.predict(X_test) # Make predictions

    # Display predictions
    print('Predictions')
    for i in range(len(X_test)):
        print(f'{'-' * 20} Prediction {i + 1} {'-' * 20}')
        print(f'Height: {X_test[i][0]} cms')
        print(f'Weight: {X_test[i][1]} kgs')
        print(f'Prediction T-Shirt Size: {predictions[i]} -> {['Medium', 'Large'][predictions[i]]}')
        print(f'{'-' * 54}')

# Entry point
if __name__ == '__main__':
    main()