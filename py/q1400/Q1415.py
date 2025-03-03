"""
 * 一个 「开心字符串」定义为：
 * 1、仅包含小写字母 ['a', 'b', 'c'].
 * 2、对所有在 1 到 s.length - 1 之间的 i ，满足 s[i] != s[i + 1] （字符串的下标从 1 开始）。
 * 比方说，字符串 "abc"，"ac"，"b" 和 "abcbabcbcb" 都是开心字符串，但是 "aa"，"baa" 和 "ababbc" 都不是开心字符串。
 * 给你两个整数 n 和 k ，你需要将长度为 n 的所有开心字符串按字典序排序。
 * 请你返回排序后的第 k 个开心字符串，如果长度为 n 的开心字符串少于 k 个，那么请你返回 空字符串 。
 * 提示：
 * 1、1 <= n <= 10
 * 2、1 <= k <= 100
 * 链接：https://leetcode.cn/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n
"""

from typing import List

INF = 0x3c3c3c3c3c3c3c3c3c

#
# @lc app=leetcode.cn id=1415 lang=python3
# @lcpr version=30005
#
# [1415] 长度为 n 的开心字符串中字典序第 k 小的字符串
#


# @lc code=start
class Solution:

    def getHappyString(self, n: int, k: int) -> str:
        if k > 3 << (n - 1):  # 3 * 2 ** (n - 1)
            return ''

        ans = ['x']
        k -= 1
        n = 1 << (n - 1)
        while n:
            order = k // n
            ans.append([x for x in 'abc' if x != ans[-1]][order])
            k %= n
            n >>= 1
        return ''.join(ans[1:])


# @lc code=end

if __name__ == '__main__':
    # "c"
    print(Solution().getHappyString(1, 3))
    # ""
    print(Solution().getHappyString(1, 4))
    # "cab"
    print(Solution().getHappyString(3, 9))
    # ""
    print(Solution().getHappyString(2, 7))
    # "abacbabacb"
    print(Solution().getHappyString(10, 100))
