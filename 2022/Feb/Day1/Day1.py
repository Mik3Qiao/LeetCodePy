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


priceIns1 = [7, 1, 5, 3, 6, 4]
priceIns2 = [7, 6, 4, 3, 1]
solution1 = Solution()
print(solution1.maxProfit(priceIns1))
print(solution1.maxProfit(priceIns2))
