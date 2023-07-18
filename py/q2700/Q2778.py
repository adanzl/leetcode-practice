"""
 * 给你一个下标从 1 开始、长度为 n 的整数数组 nums 。
 * 对 nums 中的元素 nums[i] 而言，如果 n 能够被 i 整除，即 n % i == 0 ，则认为 num[i] 是一个 特殊元素 。
 * 返回 nums 中所有 特殊元素 的 平方和 。
 * 提示：
 * 1、1 <= nums.length == n <= 50
 * 2、1 <= nums[i] <= 50
 * 链接：https://leetcode.cn/problems/sum-of-squares-of-special-elements/
"""
from typing import List


class Solution:

    def sumOfSquares(self, nums: List[int]) -> int:
        ans, n = 0, len(nums)
        for i in range(n):
            if n % (i + 1) == 0:
                ans += nums[i] * nums[i]
        return ans


if __name__ == '__main__':
    # 21
    print(Solution().sumOfSquares([1, 2, 3, 4]))
    # 63
    print(Solution().sumOfSquares([2, 7, 1, 19, 18, 3]))