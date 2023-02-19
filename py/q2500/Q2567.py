"""
 * 给你一个下标从 0 开始的整数数组 nums 。
 * 1、nums 的 最小 得分是满足 0 <= i < j < nums.length 的 |nums[i] - nums[j]| 的最小值。
 * 2、nums的 最大 得分是满足 0 <= i < j < nums.length 的 |nums[i] - nums[j]| 的最大值。
 * 3、nums 的分数是 最大 得分与 最小 得分的和。
 * 我们的目标是最小化 nums 的分数。你 最多 可以修改 nums 中 2 个元素的值。
 * 请你返回修改 nums 中 至多两个 元素的值后，可以得到的 最小分数 。
 * |x| 表示 x 的绝对值。
 * 提示：
 * 1、3 <= nums.length <= 10^5
 * 2、1 <= nums[i] <= 10^9
 * 链接：https://leetcode.cn/problems/minimum-score-by-changing-two-elements/
"""
from typing import List


class Solution:

    def minimizeSum(self, nums: List[int]) -> int:
        if len(nums) <= 2: return 0
        nums.sort()
        return min(nums[-1] - nums[2], nums[-2] - nums[1], nums[-3] - nums[0])


if __name__ == '__main__':
    # 24
    print(Solution().minimizeSum([59, 27, 9, 81, 33]))
    # 3
    print(Solution().minimizeSum([1, 4, 7, 8, 5]))
    # 0
    print(Solution().minimizeSum([1, 4, 3]))
