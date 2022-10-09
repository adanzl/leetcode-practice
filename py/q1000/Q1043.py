"""
 * 给你一个整数数组 arr，请你将该数组分隔为长度最多为 k 的一些（连续）子数组。
 * 分隔完成后，每个子数组的中的所有值都会变为该子数组中的最大值。
 * 返回将数组分隔变换后能够得到的元素最大和。
 * 注意，原数组和分隔后的数组对应顺序应当一致，也就是说，你只能选择分隔数组的位置而不能调整数组中的顺序。
 * 提示：
 * 1、1 <= arr.length <= 500
 * 2、0 <= arr[i] <= 10^9
 * 3、1 <= k <= arr.length
 * 链接：https://leetcode.cn/problems/partition-array-for-maximum-sum/
"""
from typing import List


class Solution:

    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:

        n = len(arr)
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            for j in range(1, min(k, i) + 1):
                dp[i] = max(dp[i], dp[i - j] + j * max(arr[max(0, i - j):i]))

        return dp[-1]


if __name__ == '__main__':
    # 84
    print(Solution().maxSumAfterPartitioning([1, 15, 7, 9, 2, 5, 10], 3))
    # 1
    print(Solution().maxSumAfterPartitioning([1], 1))
    # 83
    print(Solution().maxSumAfterPartitioning([1, 4, 1, 5, 7, 3, 6, 1, 9, 9, 3], 4))
