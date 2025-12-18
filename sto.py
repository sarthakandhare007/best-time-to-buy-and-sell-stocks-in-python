class Solution:
    def maxProfit(self, prices, strategy, k):
        n = len(prices)

        # Base profit
        base_profit = 0
        for i in range(n):
            base_profit += strategy[i] * prices[i]

        # Prefix sums
        prefSP = [0] * (n + 1)  # strategy[i] * prices[i]
        prefP = [0] * (n + 1)   # prices[i]

        for i in range(n):
            prefSP[i + 1] = prefSP[i] + strategy[i] * prices[i]
            prefP[i + 1] = prefP[i] + prices[i]

        half = k // 2
        max_gain = 0

        for l in range(n - k + 1):
            mid = l + half
            r = l + k

            # First half -> 0
            gain_first = -(prefSP[mid] - prefSP[l])

            # Second half -> 1
            gain_second = (prefP[r] - prefP[mid]) - (prefSP[r] - prefSP[mid])

            if gain_first + gain_second > max_gain:
                max_gain = gain_first + gain_second

        return max(base_profit, base_profit + max_gain)
