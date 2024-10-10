"""
 * 给你两个字符串 word1 和 word2 。
 * 如果一个字符串 x 重新排列后，word2 是重排字符串的 前缀 ，那么我们称字符串 x 是 合法的 。
 * 请你返回 word1 中 合法 子字符串 的数目。
 * 注意 ，这个问题中的内存限制比其他题目要 小 ，所以你 必须 实现一个线性复杂度的解法。
 * 解释：
 * 1、1 <= word1.length <= 10^6
 * 2、1 <= word2.length <= 10^4
 * 3、word1 和 word2 都只包含小写英文字母。
 * 链接：https://leetcode.cn/problems/count-substrings-that-can-be-rearranged-to-contain-a-string-ii/
"""
from typing import Counter

INF = 0x3c3c3c3c3c3c3c3c3c


class Solution:

    def validSubstringCount(self, word1: str, word2: str) -> int:
        c2 = [0] * 26
        get_v = lambda x: ord(x) - ord('a')
        for c in word2:
            c2[get_v(c)] += 1
        l, r = 0, 0
        ans = 0
        c1 = [0] * 26
        f = False
        while r < len(word1):
            c1[get_v(word1[r])] += 1
            while l < r and c1[get_v(word1[l])] > c2[get_v(word1[l])]:
                c1[get_v(word1[l])] -= 1
                l += 1
            if f or all(c1[i] >= c2[i] for i in range(26)):
                f = True
                ans += l + 1
            r += 1
        return ans


if __name__ == '__main__':
    # 10
    print(Solution().validSubstringCount("abcabc", word2="abc"))
    # 1
    print(Solution().validSubstringCount("bcca", word2="abc"))
    # 0
    print(Solution().validSubstringCount("abcabc", word2="aaabc"))
