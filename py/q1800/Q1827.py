"""
 * 链接：https://leetcode.cn/problems/minimum-operations-to-make-the-array-increasing/
"""
from typing import List


class Solution:

    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        for i in range(1, len(nums)):
            val = max(nums[i - 1] + 1 - nums[i], 0)
            ans += val
            nums[i] += val
        return ans

if __name__ == '__main__':
    # 3
    print(Solution().minOperations([1, 1, 1]))
    # 14
    print(Solution().minOperations([1, 5, 2, 4, 1]))
    # 0
    print(Solution().minOperations( [8]))