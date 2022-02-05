from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max: int = 0
        for i in range(0, len(prices) - 1):
            for j in range(i+1, len(prices)):
                result = prices[j] - prices[i]
                if result > max:
                    max = result

        return max

    def maxProfit2(self, prices: List[int]) -> int:
        maxProfit = 0;
        minPrice = float("inf")

        for i in range(len(prices)):
            if prices[i] < minPrice:
                minPrice = prices[i]
            elif (prices[i] - minPrice) > maxProfit:
                maxProfit = prices[i] - minPrice

        return maxProfit




priceIns1 = [7, 1, 5, 3, 6, 4]
priceIns2 = [7, 6, 4, 3, 1]
solutionIns = Solution()
print(solutionIns.maxProfit(priceIns1))
print(solutionIns.maxProfit(priceIns2))

print(solutionIns.maxProfit2(priceIns1))
print(solutionIns.maxProfit2(priceIns2))
