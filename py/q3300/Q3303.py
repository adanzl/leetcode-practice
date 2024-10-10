"""
 * 给你两个字符串 s 和 pattern 。
 * 如果一个字符串 x 修改 至多 一个字符会变成 y ，那么我们称它与 y 几乎相等 。
 * 请你返回 s 中下标 最小 的 子字符串 ，它与 pattern 几乎相等 。如果不存在，返回 -1 。
 * 子字符串 是字符串中的一个 非空、连续的字符序列。
 * 提示：
 * 1、1 <= pattern.length < s.length <= 10^5
 * 2、s 和 pattern 都只包含小写英文字母。
 * 链接：https://leetcode.cn/problems/find-the-occurrence-of-first-almost-equal-substring/description/
"""
from typing import List

INF = 0x3c3c3c3c3c3c3c3c3c


class Solution:

    def calc_z(self, s: str) -> list[int]:
        n = len(s)
        z = [0] * n
        box_l = box_r = 0  # z-box 左右边界
        for i in range(1, n):
            if i <= box_r:
                z[i] = min(z[i - box_l], box_r - i + 1)  # 改成手动 if 可以加快速度
            while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                box_l, box_r = i, i + z[i]
                z[i] += 1
        return z

    def minStartingIndex(self, s: str, pattern: str) -> int:
        pre_z = self.calc_z(pattern + s)
        suf_z = self.calc_z(pattern[::-1] + s[::-1])
        suf_z.reverse()  # 也可以不反转，下面写 suf_z[-i]
        m = len(pattern)
        for i in range(m, len(s) + 1):
            if pre_z[i] + suf_z[i - 1] >= m - 1:
                return i - m
        return -1


if __name__ == '__main__':
    # 0
    print(Solution().minStartingIndex("ede", pattern="d"))
    # 0
    print(Solution().minStartingIndex("dde", pattern="d"))
    # 1
    print(Solution().minStartingIndex("efeff", "fe"))
    # 3
    print(Solution().minStartingIndex("kkkkkj", "kjj"))
    # 1
    print(Solution().minStartingIndex("abcdefg", pattern="bcdffg"))
    # 4
    print(Solution().minStartingIndex("ababbababa", pattern="bacaba"))
    # -1
    print(Solution().minStartingIndex("abcd", pattern="dba"))
