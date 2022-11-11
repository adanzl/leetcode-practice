"""
 * 给你一个整数数组 arr 和一个整数 difference，请你找出并返回 arr 中最长等差子序列的长度，该子序列中相邻元素之间的差等于 difference 。
 * 子序列 是指在不改变其余元素顺序的情况下，通过删除一些元素或不删除任何元素而从 arr 派生出来的序列。
 * 提示：
 * 1、1 <= arr.length <= 10^5
 * 2、-10^4 <= arr[i], difference <= 10^4
 * 链接：https://leetcode.cn/problems/longest-arithmetic-subsequence-of-given-difference/
"""
from typing import List


class Solution:

    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        m = dict()
        for i, num in enumerate(arr):
            cnt = m.get(arr[i] - difference, 0)
            v = max(cnt + 1, m.get(arr[i], 0))
            m[arr[i]] = v
        return max(m.values())


if __name__ == '__main__':
    # 4
    print(Solution().longestSubsequence([1, 2, 3, 4], 1))
    # 1
    print(Solution().longestSubsequence([1, 3, 5, 7], 1))
    # 4
    print(Solution().longestSubsequence([1, 5, 7, 8, 5, 3, 4, 2, 1], -2))
