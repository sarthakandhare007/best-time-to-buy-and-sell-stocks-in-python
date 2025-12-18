# best-time-to-buy-and-sell-stocks-in-python
def maxProfit(prices, strategy, k):
    n = len(prices)

    # Base profit
    base = sum(strategy[i] * prices[i] for i in range(n))

    # Prefix sums
    prefSP = [0] * (n + 1)  # strategy[i] * prices[i]
    prefP = [0] * (n + 1)   # prices[i]

    for i in range(n):
        prefSP[i + 1] = prefSP[i] + strategy[i] * prices[i]
        prefP[i + 1] = prefP[i] + prices[i]

    half = k // 2
    maxGain = 0

    for l in range(n - k + 1):
        mid = l + half
        r = l + k

        # First half: set to 0
        gain_first = -(prefSP[mid] - prefSP[l])

        # Second half: set to 1
        gain_second = (prefP[r] - prefP[mid]) - (prefSP[r] - prefSP[mid])

        maxGain = max(maxGain, gain_first + gain_second)

    return max(base, base + maxGain)
