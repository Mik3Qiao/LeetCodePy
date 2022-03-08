from collections import defaultdict
from typing import List

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        # answer was wrong, because it need to done interatively instead if doing it only once

        # reference = defaultdict(int)
        # result = 0
        # total = 0
        #
        # for num in nums:
        #     reference[num] += num
        #     total += num
        #
        # points = [0] * len(reference.keys())
        # counter = 0
        # print(reference)
        # print("total is: " + str(total))
        # for i in list(reference):
        #     copyTotal = total
        #     deleted = reference[i] + reference[i - 1] + reference[i + 1]
        #     print("deleted is: " + str(deleted))
        #     copyTotal -= deleted
        #     print("copyTotal is: " + str(copyTotal))
        #     points[counter] += reference[i] + copyTotal
        #     print("points[counter] is: " + str(points[counter]))
        #     print("-----")
        #     if points[counter] > result:
        #         result = points[counter]
        #     counter += 1
        #
        # return result

        points = defaultdict(int)
        max_number = 0
        for num in nums:
            points[num] += num
            max_number = max(max_number, num)

        max_points = [0] * (max_number + 1)
        max_points[1] = points[1]

        for num in range(2, len(max_points)):
            max_points[num] = max(max_points[num - 1], max_points[num - 2] + points[num])

        return max_points[max_number]


nums = [1,1,1,2,4,5,5,5,6]
solution = Solution()
print(solution.deleteAndEarn(nums))
