def smallest_possible_sum(X):
    while True:
        # Sort the array in non-decreasing order
        X.sort()

        # Check if any transformations are possible
        transformations_possible = False

        for i in range(1, len(X)):
            if X[i] > 0 and X[i] > X[i - 1]:
                X[i] -= X[i - 1]
                transformations_possible = True

        # If no more transformations are possible, break the loop
        if not transformations_possible:
            break

    return sum(X)

# Example usage
X = [6, 9, 21]
result = smallest_possible_sum(X)
print(result)
