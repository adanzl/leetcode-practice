"""
 * 给你一个下标从 0 开始的整数数组 nums 和一个整数 k 。你需要执行以下操作 恰好 k 次，最大化你的得分：
 * 1、从 nums 中选择一个元素 m 。
 * 2、将选中的元素 m 从数组中删除。
 * 3、将新元素 m + 1 添加到数组中。
 * 4、你的得分增加 m 。
 * 请你返回执行以上操作恰好 k 次后的最大得分。
 * 提示：
 * 1、1 <= nums.length <= 100
 * 2、1 <= nums[i] <= 100
 * 3、1 <= k <= 100
 * 链接：https://leetcode.cn/problems/maximum-sum-with-exactly-k-elements
"""
from typing import List


class Solution:

    def maximizeSum(self, nums: List[int], k: int) -> int:
        return max(nums) * k + (k - 1) * k // 2


if __name__ == '__main__':
    # 18
    print(Solution().maximizeSum([1, 2, 3, 4, 5], k=3))
    # 11
    print(Solution().maximizeSum([5, 5, 5], k=2))
