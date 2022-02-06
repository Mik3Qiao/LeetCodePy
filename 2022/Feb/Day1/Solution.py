from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max: int = 0
        for i in range(0, len(prices) - 1):
            for j in range(i + 1, len(prices)):
                result = prices[j] - prices[i]
                if result > max:
                    max = result

        return max

    def maxProfit2(self, prices: List[int]) -> int:
        maxProfit = 0
        minPrice = float("inf")

        for i in range(len(prices)):
            if prices[i] < minPrice:
                minPrice = prices[i]
            elif (prices[i] - minPrice) > maxProfit:
                maxProfit = prices[i] - minPrice

        return maxProfit
    

def run():
    priceIns1 = [7, 1, 5, 3, 6, 4]
    priceIns2 = [7, 6, 4, 3, 1]
    solutionIns = Solution()
    if (solutionIns.maxProfit(priceIns1) == 5) and (solutionIns.maxProfit(priceIns2) == 0):
        print("Day 1: solution 1 Passed")
    else:
        raise RuntimeError("Day 1 solution 1 failed")

    if (solutionIns.maxProfit2(priceIns1) == 5) and (solutionIns.maxProfit2(priceIns2) == 0):
        print("Day 1: solution 2 Passed")
    else:
        raise RuntimeError("Day 1 solution 2 failed")
    
    