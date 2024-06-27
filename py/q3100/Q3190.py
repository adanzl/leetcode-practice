"""
 * 给你一个整数数组 nums 。一次操作中，你可以将 nums 中的 任意 一个元素增加或者减少 1 。
 * 请你返回将 nums 中所有元素都可以被 3 整除的 最少 操作次数。
 * 提示：
 * 1、1 <= nums.length <= 50
 * 2、1 <= nums[i] <= 50
 * 链接：https://leetcode.cn/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/
"""
from typing import List


class Solution:

    def minimumOperations(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            r = num % 3
            ans += int(bool(r))
        return ans


if __name__ == '__main__':
    # 3
    print(Solution().minimumOperations([1, 2, 3, 4]))
    # 0
    print(Solution().minimumOperations([3, 6, 9]))
