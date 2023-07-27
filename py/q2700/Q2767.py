"""
 * 给你一个二进制字符串 s ，你需要将字符串分割成一个或者多个 子字符串  ，使每个子字符串都是 美丽 的。
 * 如果一个字符串满足以下条件，我们称它是 美丽 的：
 * 1、它不包含前导 0 。
 * 2、它是 5 的幂的 二进制 表示。
 * 请你返回分割后的子字符串的 最少 数目。如果无法将字符串 s 分割成美丽子字符串，请你返回 -1 。
 * 子字符串是一个字符串中一段连续的字符序列。
 * 提示：
 * 1、1 <= s.length <= 15
 * 2、s[i] 要么是 '0' 要么是 '1' 。
 * 链接：https://leetcode.cn/problems/partition-string-into-minimum-beautiful-substrings/
"""
from functools import cache

s5 = set()
for i in range(10):
    s5.add(bin(5**i)[2:])

class Solution:

    def minimumBeautifulSubstrings(self, s: str) -> int:

        @cache
        def func(s):
            if s[0] == '0': return -1
            if s in s5: return 1

            ans = len(s)
            find = False
            for i in range(1, len(s)):
                l1, l2 = func(s[:i]), func(s[i:])
                if l1 == -1 or l2 == -1: continue
                ans = min(ans, l1 + l2)
                find = True
            return ans if find else -1

        return func(s)


if __name__ == '__main__':
    # -1
    print(Solution().minimumBeautifulSubstrings("10"))
    # 6
    print(Solution().minimumBeautifulSubstrings("101101111101"))
    # 2
    print(Solution().minimumBeautifulSubstrings("1011"))
    # 3
    print(Solution().minimumBeautifulSubstrings("111"))
    # -1
    print(Solution().minimumBeautifulSubstrings("0"))