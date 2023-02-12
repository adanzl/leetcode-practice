"""
 * 给你两个整数数组 nums1 和 nums2 ，它们长度都为 n 。
 * 两个数组的 异或值之和 为 (nums1[0] XOR nums2[0]) + (nums1[1] XOR nums2[1]) + ... + (nums1[n - 1] XOR nums2[n - 1]) （下标从 0 开始）。
 * 比方说，[1,2,3] 和 [3,2,1] 的 异或值之和 等于 (1 XOR 3) + (2 XOR 2) + (3 XOR 1) = 2 + 0 + 2 = 4 。
 * 请你将 nums2 中的元素重新排列，使得 异或值之和 最小 。
 * 请你返回重新排列之后的 异或值之和 。
 * 提示：
 * 1、n == nums1.length
 * 2、n == nums2.length
 * 3、1 <= n <= 14
 * 4、0 <= nums1[i], nums2[i] <= 10^7
 * 链接：https://leetcode.cn/problems/minimum-xor-sum-of-two-arrays/
"""
from typing import List


class Solution:

    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        dp = [0x3c3c3c3c] * (1 << n)
        dp[0] = 0
        for i in range(1, 1 << n):
            for j in range(i.bit_length()):
                if i & (1 << j) == 0: continue
                dp[i] = min(dp[i], dp[i ^ (1 << j)] + (nums2[j] ^ nums1[i.bit_count() - 1]))
        return dp[-1]


if __name__ == '__main__':
    # 2
    print(Solution().minimumXORSum([1, 2], [2, 3]))
    # 8
    print(Solution().minimumXORSum([1, 0, 3], [5, 3, 4]))