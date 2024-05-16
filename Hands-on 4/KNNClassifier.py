from DiscreteMaths import DiscreteMaths

class KNNClassifier:
    def __init__(self, k = 5, metric = 'euclidean'):
        self.k = k
        self.metric = metric

    # Training dara
    def fit(self, X_train, y_train):
        self.X_train = X_train
        self.y_train = y_train
        self.dm = DiscreteMaths(len(X_train[0]))

    # Make predictions based on training data
    def predict(self, X_test):
        distances = self._compute_distances(X_test)
        nearest_neighbors = self._get_nearest_neighbors(distances)
        predictions = self._majority_vote(nearest_neighbors)

        return predictions

    # Compute distances between test and training data
    def _compute_distances(self, X_test):
        distances = []

        for x_test in X_test:
            distances_i = []

            for x_train in self.X_train:
                distance = self._calculate_distance(x_test, x_train)
                distances_i.append(distance)

            distances.append(distances_i)

        return distances

    # Calculate distance between two points
    def _calculate_distance(self, x1, x2):
        if self.metric == 'euclidean':
            return self.dm.euclidean_distance(x1, x2)

        elif self.metric == 'manhattan':
            return self.dm.manhattan_distance(x1, x2)

    # Get nearest neighbors based on distances
    def _get_nearest_neighbors(self, distances):
        nearest_neighbors = []

        for distances_i in distances:
            indices = []

            for i in range(len(distances_i)):
                min_distance = distances_i[0]
                min_index = 0

                # Find the minimum distance
                for j in range(1, len(distances_i)):
                    if distances_i[j] < min_distance:
                        min_distance = distances_i[j]
                        min_index = j

                indices.append(min_index)

            # Get the k nearest neighbors
            if len(indices) > self.k:
                indices = indices[:self.k]

            nearest_neighbors_i = []

            for i in indices:
                nearest_neighbors_i.append(self.y_train[i])

            nearest_neighbors.append(nearest_neighbors_i)

        return nearest_neighbors

    # Get the majority vote
    def _majority_vote(self, nearest_neighbors):
        predictions = []

        # Get the majority vote for each nearest neighbor
        for nearest_neighbors_i in nearest_neighbors:
            vote_counts = {}

            for label in nearest_neighbors_i:
                if label not in vote_counts:
                    vote_counts[label] = 0

                vote_counts[label] += 1

            max_votes = 0
            max_label = None

            # Get the label with the most votes
            for label, votes in vote_counts.items():
                if votes > max_votes:
                    max_votes = votes
                    max_label = label

            predictions.append(max_label)

        return predictions