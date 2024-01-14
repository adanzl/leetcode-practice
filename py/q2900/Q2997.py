"""
 * 给你一个下标从 0 开始的整数数组 nums 和一个正整数 k 。
 * 你可以对数组执行以下操作 任意次 ：
 *      选择数组里的 任意 一个元素，并将它的 二进制 表示 翻转 一个数位，翻转数位表示将 0 变成 1 或者将 1 变成 0 。
 * 你的目标是让数组里 所有 元素的按位异或和得到 k ，请你返回达成这一目标的 最少 操作次数。
 * 注意，你也可以将一个数的前导 0 翻转。比方说，数字 (101)2 翻转第四个数位，得到 (1101)2 。
 * 提示：
 * 1、1 <= nums.length <= 10^5
 * 2、0 <= nums[i] <= 10^6
 * 3、0 <= k <= 10^6
 * 链接：https://leetcode.cn/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k/
"""
from typing import List


class Solution:

    def minOperations(self, nums: List[int], k: int) -> int:
        cnt = 0
        for num in nums:
            for i in range(num.bit_length()):
                if num & 1 << i:
                    cnt ^= (1 << i)
        ans = 0
        for i in range(max(cnt.bit_length(), k.bit_length())):
            if cnt & 1 << i != k & 1 << i:
                ans += 1
        return ans


if __name__ == '__main__':
    # 3
    print(Solution().minOperations([9, 7, 9, 14, 8, 6], 12))
    # 2
    print(Solution().minOperations([2, 1, 3, 4], k=1))
    # 0
    print(Solution().minOperations([2, 0, 2, 0], k=0))
