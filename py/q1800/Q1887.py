"""
 * 给你一个整数数组 nums ，你的目标是令 nums 中的所有元素相等。完成一次减少操作需要遵照下面的几个步骤：
 * 1、找出 nums 中的 最大 值。记这个值为 largest 并取其下标 i （下标从 0 开始计数）。如果有多个元素都是最大值，则取最小的 i 。
 * 2、找出 nums 中的 下一个最大 值，这个值 严格小于 largest ，记为 nextLargest 。
 * 将 nums[i] 减少到 nextLargest 。
 * 返回使 nums 中的所有元素相等的操作次数。
 * 提示：
 * 1、1 <= nums.length <= 5 * 10^4
 * 2、1 <= nums[i] <= 5 * 10^4
 * 链接：https://leetcode.cn/problems/reduction-operations-to-make-the-array-elements-equal/
"""
from typing import List


class Solution:

    def reductionOperations(self, nums: List[int]) -> int:
        pre, n_pre = -1, 0
        ans = 0
        for num in sorted(nums, reverse=True):
            if num == pre:
                n_pre += 1
            else:
                ans += n_pre
                n_pre += 1
                pre = num
        return ans


if __name__ == '__main__':
    # 3
    print(Solution().reductionOperations([5, 1, 3]))
    # 0
    print(Solution().reductionOperations([1, 1, 1]))
    # 4
    print(Solution().reductionOperations([1, 1, 2, 2, 3]))
