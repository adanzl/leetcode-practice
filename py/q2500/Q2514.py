"""
 * 给你一个字符串 s ，它包含一个或者多个单词。单词之间用单个空格 ' ' 隔开。
 * 如果字符串 t 中第 i 个单词是 s 中第 i 个单词的一个 排列 ，那么我们称字符串 t 是字符串 s 的同位异构字符串。
 * 比方说，"acb dfe" 是 "abc def" 的同位异构字符串，但是 "def cab" 和 "adc bef" 不是。
 * 请你返回 s 的同位异构字符串的数目，由于答案可能很大，请你将它对 10^9 + 7 取余 后返回。
 * 提示：
 * 1、1 <= s.length <= 10^5
 * 2、s 只包含小写英文字母和空格 ' ' 。
 * 3、相邻单词之间由单个空格隔开。
 * 链接：https://leetcode.cn/problems/count-anagrams/
"""
from collections import Counter
from math import factorial


class Solution:

    def countAnagrams(self, s: str) -> int:
        MOD = 10**9 + 7
        arr = s.split()
        cnt = []

        for w in arr:
            c = Counter(w)
            v = factorial(len(w))
            for vv in c.values():
                v //= factorial(vv)
            cnt.append(v)
        ans = 1
        for v in cnt:
            ans *= v
            ans %= MOD
        return ans


if __name__ == '__main__':
    # 18
    print(Solution().countAnagrams("too hot"))
    # 1
    print(Solution().countAnagrams("aa"))