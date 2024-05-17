class DiscreteMaths:
    def __init__(self) -> None:
        pass

    # Standardize data
    def standardize(self, data: list[float]) -> list[float]:
        # Getting heights and weights from data
        heights: list[float] = [data[i][0] for i in range(len(data))]
        weights: list[float] = [data[i][1] for i in range(len(data))]

        std_heights: list[float] = []
        std_weights: list[float] = []

        # Standardizing heights and weights based on
        # Xs = (X - min) / (max - min)
        for i in range(len(data)):
            std_heights.append((heights[i] - min(heights)) / (max(heights) - min(heights)))
            std_weights.append((weights[i] - min(weights)) / (max(weights) - min(weights)))

        # Regrouping standardized heights and weights
        return [[std_heights[i], std_weights[i]] for i in range(len(data))]

    # Euclidean Distance
    def euclidean_distance(self, x1: list[float], x2: list[float]) -> float:
        distance = 0

        for i in range(len(x1)):
            distance += (x1[i] - x2[i]) ** 2

        return distance ** 0.5

    # Manhattan Distance
    def manhattan_distance(self, x1: list[float], x2: list[float]) -> float:
        distance = 0

        for i in range(len(x1)):
            distance += abs(x1[i] - x2[i])

        return distance