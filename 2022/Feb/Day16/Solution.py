from typing import List

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        resultArr = [0] * len(nums)

        sum = 0
        for i in range(2, len(resultArr)):
            if (nums[i] - nums[i-1]) == (nums[i-1] - nums[i-2]):
                resultArr[i] = 1 + resultArr[i-1]
                sum += resultArr[i]

        return sum