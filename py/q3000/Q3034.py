"""
 * 给你一个下标从 0 开始长度为 n 的整数数组 nums ，和一个下标从 0 开始长度为 m 的整数数组 pattern ，pattern 数组只包含整数 -1 ，0 和 1 。
 * 大小为 m + 1 的子数组 nums[i..j] 如果对于每个元素 pattern[k] 都满足以下条件，那么我们说这个子数组匹配模式数组 pattern ：
 * 1、如果 pattern[k] == 1 ，那么 nums[i + k + 1] > nums[i + k]
 * 2、如果 pattern[k] == 0 ，那么 nums[i + k + 1] == nums[i + k]
 * 3、如果 pattern[k] == -1 ，那么 nums[i + k + 1] < nums[i + k]
 * 请你返回匹配 pattern 的 nums 子数组的 数目 。
 * 提示：
 * 1、2 <= n == nums.length <= 100
 * 2、1 <= nums[i] <= 10^9
 * 3、1 <= m == pattern.length < n
 * 4、-1 <= pattern[i] <= 1
 * 链接：https://leetcode.cn/problems/number-of-subarrays-that-match-a-pattern-i/
"""
from itertools import pairwise
from typing import List


class Solution:

    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        # kmp 构建next数组
        def build_next(ss):
            next_arr = [0] * len(ss)
            c = 0
            for i in range(1, len(ss)):
                v = ss[i]
                while c and ss[c] != v:
                    c = next_arr[c - 1]
                if ss[c] == v:
                    c += 1
                next_arr[i] = c
            return next_arr

        s = []
        for a, b in pairwise(nums):
            if a == b:
                s.append(0)
            elif a > b:
                s.append(-1)
            else:
                s.append(1)
        next_arr = build_next(pattern)
        c, ans = 0, 0
        for v in s:
            while c and pattern[c] != v:
                c = next_arr[c - 1]
            if pattern[c] == v:
                c += 1
            if c == len(pattern):
                ans += 1
                c = next_arr[c - 1]
        return ans


if __name__ == '__main__':
    # 4
    print(Solution().countMatchingSubarrays([1, 2, 3, 4, 5, 6], pattern=[1, 1]))
    # 2
    print(Solution().countMatchingSubarrays([1, 4, 4, 1, 3, 5, 5, 3], pattern=[1, 0, -1]))
