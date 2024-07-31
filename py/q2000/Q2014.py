"""
 * 给你一个长度为 n 的字符串 s ，和一个整数 k 。请你找出字符串 s 中 重复 k 次的 最长子序列 。
 * 子序列 是由其他字符串删除某些（或不删除）字符派生而来的一个字符串。
 * 如果 seq * k 是 s 的一个子序列，其中 seq * k 表示一个由 seq 串联 k 次构造的字符串，
 * 那么就称 seq 是字符串 s 中一个 重复 k 次 的子序列。
 * 举个例子，"bba" 是字符串 "bababcba" 中的一个重复 2 次的子序列，
 * 因为字符串 "bbabba" 是由 "bba" 串联 2 次构造的，而 "bbabba" 是字符串 "bababcba" 的一个子序列。
 * 返回字符串 s 中 重复 k 次的最长子序列  。如果存在多个满足的子序列，则返回 字典序最大 的那个。
 * 如果不存在这样的子序列，返回一个 空 字符串。
 * 提示：
 * 1、n == s.length
 * 2、2 <= k <= 2000
 * 3、2 <= n < k * 8
 * 4、s 由小写英文字母组成
 * 链接：https://leetcode.cn/problems/longest-subsequence-repeated-k-times/
"""

from collections import deque
from typing import Counter

#
# @lc app=leetcode.cn id=2014 lang=python3
#
# [2014] 重复 K 次的最长子序列
#


# @lc code=start
class Solution:

    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        arr, q = [], deque()
        for v, c in Counter(s).items():
            if c >= k:
                arr.append(v)
                q.append(v)
        ans = ""

        def valid(txt):
            i0, i1 = 0, 0
            while i0 < len(txt) and i1 < len(s):
                if txt[i0] == s[i1]:
                    i0 += 1
                i1 += 1
            return i0 == len(txt)

        # 遍历全排列
        while q:
            s_size = len(q)
            for _ in range(s_size):
                ls = q.popleft()
                if len(ls) > len(ans) or (len(ls) == len(ans) and ls > ans):
                    ans = ls
                for sc in arr:
                    cur_s = ls + sc
                    if valid(cur_s * k):
                        q.append(cur_s)

        return ans


# @lc code=end

if __name__ == '__main__':
    # "let"
    print(Solution().longestSubsequenceRepeatedK("letsleetcode", k=2))
    # "b"
    print(Solution().longestSubsequenceRepeatedK("bb", k=2))
    # ""
    print(Solution().longestSubsequenceRepeatedK("ab", k=2))
