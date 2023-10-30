def knapsack(weights, values, capacity):
    n = len(values)
    dp = [0] * (capacity + 1)

    for i in range(n):
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], values[i] + dp[w - weights[i]])

    result = []
    w = capacity
    for i in range(n - 1, -1, -1):
        if dp[w] != dp[w - weights[i]] + values[i]:
            result.append(i)
            w -= weights[i]

    return dp[capacity], result[::-1]

# Example usage
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50
max_value, indices = knapsack(weights, values, capacity)
print(f"Maximum value: {max_value}")
print(f"Indices of chosen items: {indices}")
