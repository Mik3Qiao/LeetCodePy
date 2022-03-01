from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0] * (n + 1)
        for i in range(1, len(result)):
            result[i] = result[i >> 1] + (i & 1)
        return result
