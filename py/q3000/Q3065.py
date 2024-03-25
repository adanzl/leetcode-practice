"""
 * 给你一个下标从 0 开始的整数数组 nums 和一个整数 k 。
 * 一次操作中，你可以删除 nums 中的最小元素。
 * 你需要使数组中的所有元素都大于或等于 k ，请你返回需要的 最少 操作次数。
 * 提示：
 * 1、1 <= nums.length <= 50
 * 2、1 <= nums[i] <= 10^9
 * 3、1 <= k <= 10^9
 * 4、输入保证至少有一个满足 nums[i] >= k 的下标 i 存在。
 * 链接：https://leetcode.cn/problems/minimum-operations-to-exceed-threshold-value-i/
"""
import bisect
from typing import List


class Solution:

    def minOperations(self, nums: List[int], k: int) -> int:
        return bisect.bisect_left(sorted(nums), k)


if __name__ == '__main__':
    # 3
    print(Solution().minOperations([2, 11, 10, 1, 3], k=10))
    # 0
    print(Solution().minOperations([1, 1, 2, 4, 9], k=1))
    # 4
    print(Solution().minOperations([1, 1, 2, 4, 9], k=9))
