def knapsack(weights, values, capacity):
    n = len(values)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    result = []
    w, v = capacity, dp[n][capacity]
    for i in range(n, 0, -1):
        if v <= 0:
            break
        if v == dp[i - 1][w]:
            continue
        else:
            result.append(i - 1)
            v -= values[i - 1]
            w -= weights[i - 1]

    return dp[n][capacity], result

# Example usage
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50
max_value, indices = knapsack(weights, values, capacity)
print(f"Maximum value: {max_value}")
print(f"Indices of chosen items: {indices}")
