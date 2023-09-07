"""
 * 给你一个下标从 0 开始长度为 n 的整数数组 nums 。
 * 从 0 到 n - 1 的数字被分为编号从 1 到 3 的三个组，数字 i 属于组 nums[i] 。注意，有的组可能是 空的 。
 * 你可以执行以下操作任意次：
 * 选择数字 x 并改变它的组。更正式的，你可以将 nums[x] 改为数字 1 到 3 中的任意一个。
 * 你将按照以下过程构建一个新的数组 res ：
 * 1、将每个组中的数字分别排序。
 * 2、将组 1 ，2 和 3 中的元素 依次 连接以得到 res 。
 * 如果得到的 res 是 非递减顺序的，那么我们称数组 nums 是 美丽数组 。
 * 请你返回将 nums 变为 美丽数组 需要的最少步数。
 * 提示：
 * 1、1 <= nums.length <= 100
 * 2、1 <= nums[i] <= 3
 * 链接：https://leetcode.cn/problems/sorting-three-groups/
"""
from typing import List


class Solution:

    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0] * 3 for _ in range(n + 1)]
        for i, num in enumerate(nums):
            dp[i + 1][0] = dp[i][0] + (0 if num == 1 else 1)  # 1
            dp[i + 1][1] = min(dp[i][0], dp[i][1]) + (0 if num == 2 else 1)  # 2
            dp[i + 1][2] = min(dp[i][0], dp[i][1], dp[i][2]) + (0 if num == 3 else 1)  # 3
        return min(dp[-1])


if __name__ == '__main__':
    # 3
    print(Solution().minimumOperations([2, 1, 3, 2, 1]))
    # 2
    print(Solution().minimumOperations([1, 3, 2, 1, 3, 3]))
    # 0
    print(Solution().minimumOperations([2, 2, 2, 2, 3, 3]))
