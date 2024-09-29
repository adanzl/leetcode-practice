"""
 * 给你一个字符串 word 和一个 非负 整数 k。
 * 返回 word 的 子字符串 中，每个元音字母（'a'、'e'、'i'、'o'、'u'）至少 出现一次，并且 恰好 包含 k 个辅音字母的子字符串的总数。
 * 提示：
 * 1、5 <= word.length <= 2 * 10^5
 * 2、word 仅由小写英文字母组成。
 * 3、0 <= k <= word.length - 5
 * 链接：https://leetcode.cn/problems/count-of-substrings-containing-every-vowel-and-k-consonants-ii/
"""
from typing import Counter

INF = 0x3c3c3c3c3c3c3c3c3c


class Solution:
    # 每个元音字母至少出现一次，并且至少包含 k 个辅音字母的子字符串的总数
    def f(self, word: str, k: int) -> int:
        cnt1 = Counter()  # 元音
        ans = cnt2 = left = 0  # cnt2 维护辅音
        for c in word:
            if c in "aeiou":
                cnt1[c] += 1
            else:
                cnt2 += 1
            while len(cnt1) == 5 and cnt2 >= k:
                out = word[left]
                if out in "aeiou":
                    cnt1[out] -= 1
                    if cnt1[out] == 0:
                        del cnt1[out]
                else:
                    cnt2 -= 1
                left += 1
            ans += left
        return ans

    def countOfSubstrings(self, word: str, k: int) -> int:
        return self.f(word, k) - self.f(word, k + 1)


if __name__ == '__main__':
    # 3
    print(Solution().countOfSubstrings("ieaouqqieaouqq", k=1))
    # 1
    print(Solution().countOfSubstrings("aeiou", k=0))
    # 0
    print(Solution().countOfSubstrings("aeioqq", k=1))
