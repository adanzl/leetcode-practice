"""
 * 给你一个整数数组 nums ，返回 nums 中所有 等差子序列 的数目。
 * 如果一个序列中 至少有三个元素 ，并且任意两个相邻元素之差相同，则称该序列为等差序列。
 * 1、例如，[1, 3, 5, 7, 9]、[7, 7, 7, 7] 和 [3, -1, -5, -9] 都是等差序列。
 * 2、再例如，[1, 1, 2, 5, 7] 不是等差序列。
 * 数组中的子序列是从数组中删除一些元素（也可能不删除）得到的一个序列。
 * 例如，[2,5,10] 是 [1,2,1,2,4,1,5,10] 的一个子序列。
 * 题目数据保证答案是一个 32-bit 整数。
 * 提示：
 * 1、1 <= nums.length <= 1000
 * 2、-2^31 <= nums[i] <= 2^31 - 1
 * 链接：https://leetcode.cn/problems/arithmetic-slices-ii-subsequence/
"""
from collections import Counter
from typing import List


class Solution:

    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        dp2 = [Counter() for _ in range(n)]
        ans = 0
        for i in range(n):
            for j in range(i):
                d = nums[i] - nums[j]
                cnt = dp2[j][d]
                ans += cnt
                dp2[i][d] += cnt + 1
        return ans


if __name__ == '__main__':
    # 16
    print(Solution().numberOfArithmeticSlices([7, 7, 7, 7, 7]))
    # 2
    print(Solution().numberOfArithmeticSlices([2, 2, 3, 4]))
    # 7
    print(Solution().numberOfArithmeticSlices([2, 4, 6, 8, 10]))
    # 0
    print(Solution().numberOfArithmeticSlices([0, 2000000000, -294967296]))
