"""
 * 给你一个下标从 0 开始的整数数组 nums 和一个整数 k 。
 * 请你用整数形式返回 nums 中的特定元素之 和 ，这些特定元素满足：其对应下标的二进制表示中恰存在 k 个置位。
 * 整数的二进制表示中的 1 就是这个整数的 置位 。
 * 例如，21 的二进制表示为 10101 ，其中有 3 个置位。
 * 提示：
 * 1、1 <= nums.length <= 1000
 * 2、1 <= nums[i] <= 10^5
 * 3、0 <= k <= 10
 * 链接：https://leetcode.cn/problems/sum-of-values-at-indices-with-k-set-bits/
"""
from typing import List


class Solution:

    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        return sum([num for i, num in enumerate(nums) if i.bit_count() == k])


if __name__ == '__main__':
    # 13
    print(Solution().sumIndicesWithKSetBits([5, 10, 1, 5, 2], k=1))
    # 1
    print(Solution().sumIndicesWithKSetBits([4, 3, 2, 1], k=2))
