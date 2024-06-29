"""
 * 你有一个初始为空的浮点数数组 averages。另给你一个包含 n 个整数的数组 nums，其中 n 为偶数。
 * 你需要重复以下步骤 n / 2 次：
 * 1、从 nums 中移除 最小 的元素 minElement 和 最大 的元素 maxElement。
 * 2、将 (minElement + maxElement) / 2 加入到 averages 中。
 * 返回 averages 中的 最小 元素。
 * 提示：
 * 1、2 <= n == nums.length <= 50
 * 2、n 为偶数。
 * 3、1 <= nums[i] <= 50
 * 链接：https://leetcode.cn/problems/minimum-average-of-smallest-and-largest-elements/
"""
from typing import List


class Solution:

    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        n = len(nums)
        return min([(nums[i] + nums[n - i - 1]) / 2 for i in range(n // 2)])


if __name__ == '__main__':
    # 5.5
    print(Solution().minimumAverage([7, 8, 3, 4, 15, 13, 4, 1]))
    # 5.5
    print(Solution().minimumAverage([1, 9, 8, 3, 10, 5]))
    # 5.0
    print(Solution().minimumAverage([1, 2, 3, 7, 8, 9]))
