"""
 * 给你一个长度为 3 的整数数组 nums。
 * 现以某种顺序 连接 数组 nums 中所有元素的 二进制表示 ，请你返回可以由这种方法形成的 最大 数值。
 * 注意 任何数字的二进制表示 不含 前导零。
 * 提示:
 * 1、nums.length == 3
 * 2、1 <= nums[i] <= 127
 * 链接：https://leetcode.cn/problems/maximum-possible-number-by-binary-concatenation/
"""
from functools import cmp_to_key
from typing import List

INF = 0x3c3c3c3c3c3c3c3c3c


class Solution:

    def maxGoodNumber(self, nums: List[int]) -> int:

        def cmp(x, y):
            s1, s2 = x + y, y + x
            if s1 == s2: return 0
            if s1 > s2: return -1
            return 1

        return int(''.join(sorted([bin(num)[2:] for num in nums], key=cmp_to_key(cmp))), 2)


if __name__ == '__main__':
    # 221
    print(Solution().maxGoodNumber([1, 11, 5]))
    # 1906
    print(Solution().maxGoodNumber([1, 18, 27]))
    # 230
    print(Solution().maxGoodNumber([1, 38, 1]))
    # 30
    print(Solution().maxGoodNumber([1, 2, 3]))
    # 1296
    print(Solution().maxGoodNumber([2, 8, 16]))
