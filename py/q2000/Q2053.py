"""
 * 独一无二的字符串 指的是在一个数组中只出现过 一次 的字符串。
 * 给你一个字符串数组 arr 和一个整数 k ，请你返回 arr 中第 k 个 独一无二的字符串 。
 * 如果 少于 k 个独一无二的字符串，那么返回 空字符串 "" 。
 * 注意，按照字符串在原数组中的 顺序 找到第 k 个独一无二字符串。
 * 提示：
 * 1、1 <= k <= arr.length <= 1000
 * 2、1 <= arr[i].length <= 5
 * 3、arr[i] 只包含小写英文字母。
 * 链接：https://leetcode.cn/problems/kth-distinct-string-in-an-array/
"""

from typing import Counter, List

#
# @lc app=leetcode.cn id=2053 lang=python3
#
# [2053] 数组中第 K 个独一无二的字符串
#


# @lc code=start
class Solution:

    def kthDistinct(self, arr: List[str], k: int) -> str:
        cnt = Counter(arr)
        ii = 0
        for s in arr:
            if cnt[s] == 1:
                ii += 1
            if ii == k:
                return s
        return ''


# @lc code=end

if __name__ == '__main__':
    # "a"
    print(Solution().kthDistinct(["d", "b", "c", "b", "c", "a"], k=2))
    # "aaa"
    print(Solution().kthDistinct(["aaa", "aa", "a"], k=1))
    # ""
    print(Solution().kthDistinct(["a", "b", "a"], k=3))
