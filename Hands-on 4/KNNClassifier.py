from DiscreteMaths import DiscreteMaths

class KNNClassifier:
    def __init__(self, k = 5, metric = 'euclidean') -> None:
        self.k: int = k
        self.metric: str = metric

    # Training dara
    def fit(self, X_train, y_train) -> None:
        self.X_train: list[float] = X_train
        self.y_train: list[float] = y_train
        self.dm: DiscreteMaths = DiscreteMaths()

        # Standardize training data
        self.x_train_std: list[float] = self.dm.standardize(X_train)

    # Make predictions based on training data
    def predict(self, X_test) -> list[int]:
        # Standardize test data
        x_test_std: list[float] = self.dm.standardize(X_test)

        distances: list[float] = self._compute_distances(x_test_std)
        nearest_neighbors: list[float] = self._get_nearest_neighbors(distances)
        predictions: list[int] = self._majority_vote(nearest_neighbors)

        return predictions

    # Compute distances between test and training data
    def _compute_distances(self, X_test: list[float]) -> list[float]:
        distances: list[float] = []

        for x_test in X_test:
            distances_i: list[float] = []

            for x_train in self.x_train_std:
                distance: float = self._calculate_distance(x_test, x_train)
                distances_i.append(distance)

            distances.append(distances_i)

        return distances

    # Calculate distance between two points
    def _calculate_distance(self, x1: list[float], x2: list[float]) -> float:
        if self.metric == 'euclidean':
            return self.dm.euclidean_distance(x1, x2)

        elif self.metric == 'manhattan':
            return self.dm.manhattan_distance(x1, x2)

        else:
            raise ValueError('Invalid metric')

    # Get nearest neighbors based on distances
    def _get_nearest_neighbors(self, distances: list[float]) -> list[float]:
        nearest_neighbors: list[float] = []

        for distances_i in distances:
            indexes: list[float] = []

            for i in range(len(distances_i)):
                min_distance: float = distances_i[0]
                min_index: int = 0

                # Find the minimum distance
                for j in range(1, len(distances_i)):
                    if distances_i[j] < min_distance:
                        min_distance = distances_i[j]
                        min_index = j

                indexes.append(min_index)

            # Get the k nearest neighbors
            if len(indexes) > self.k:
                indexes = indexes[:self.k]

            nearest_neighbors_i: list[int] = []

            for i in indexes:
                nearest_neighbors_i.append(self.y_train[i])

            nearest_neighbors.append(nearest_neighbors_i)

        return nearest_neighbors

    # Get the majority vote
    def _majority_vote(self, nearest_neighbors: list[float]) -> list[int]:
        predictions: list[int] = []

        # Get the majority vote for each nearest neighbor
        for nearest_neighbors_i in nearest_neighbors:
            vote_counts = {}

            for label in nearest_neighbors_i:
                if label not in vote_counts:
                    vote_counts[label] = 0

                vote_counts[label] += 1

            max_votes: int = 0
            max_label: int = None

            # Get the label with the most votes
            for label, votes in vote_counts.items():
                if votes > max_votes:
                    max_votes = votes
                    max_label = label

            predictions.append(max_label)

        return predictions