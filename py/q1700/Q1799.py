"""
 * 给你 nums ，它是一个大小为 2 * n 的正整数数组。你必须对这个数组执行 n 次操作。
 * 在第 i 次操作时（操作编号从 1 开始），你需要：
 * 1、选择两个元素 x 和 y 。
 * 2、获得分数 i * gcd(x, y) 。
 * 3、将 x 和 y 从 nums 中删除。
 * 请你返回 n 次操作后你能获得的分数和最大为多少。
 * 函数 gcd(x, y) 是 x 和 y 的最大公约数。
 * 提示：
 * 1、1 <= n <= 7
 * 2、nums.length == 2 * n
 * 3、1 <= nums[i] <= 10^6
 * 链接：https://leetcode.cn/problems/maximize-score-after-n-operations/
"""
from typing import List
from math import gcd
from functools import cache

class Solution:

    def maxScore(self, nums: List[int]) -> int:
        n = len(nums) // 2
        
        @cache
        def f(state, idx):
            if idx == n: return 0
            mx, l = 0, state.bit_length()
            for i in range(l):
                if not state & 1<< i: continue
                for j in range(i + 1, l):
                    if not state & 1 << j: continue
                    mx = max(mx, gcd(nums[i], nums[j]) * (idx + 1) + f(state & ~(1 << i | 1 << j), idx + 1))
            return mx
        return f((1 << len(nums)) - 1, 0)


if __name__ == '__main__':
    # 1
    print(Solution().maxScore([1, 2]))
    # 11
    print(Solution().maxScore([3, 4, 6, 8]))
    # 14
    print(Solution().maxScore([1, 2, 3, 4, 5, 6]))
