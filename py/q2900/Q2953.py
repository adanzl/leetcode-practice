"""
 * 给你一个字符串 word 和一个整数 k 。
 * 如果 word 的一个子字符串 s 满足以下条件，我们称它是 完全字符串：
 * 1、s 中每个字符 恰好 出现 k 次。
 * 2、相邻字符在字母表中的顺序 至多 相差 2 。也就是说，s 中两个相邻字符 c1 和 c2 ，它们在字母表中的位置相差 至多 为 2 。
 * 请你返回 word 中 完全 子字符串的数目。
 * 子字符串 指的是一个字符串中一段连续 非空 的字符序列。
 * 提示：
 * 1、1 <= word.length <= 10^5
 * 2、word 只包含小写英文字母。
 * 3、1 <= k <= word.length
 * 链接：https://leetcode.cn/problems/count-complete-substrings/description/
"""
from collections import Counter


class Solution:

    def countCompleteSubstrings(self, word: str, k: int) -> int:

        def f(s: str) -> int:
            res = 0
            for m in range(1, 27):
                if k * m > len(s):
                    break
                cnt = Counter()
                for right, c in enumerate(s):
                    cnt[c] += 1
                    left = right + 1 - k * m
                    if left >= 0:
                        res += all(c == 0 or c == k for c in cnt.values())
                        cnt[s[left]] -= 1
            return res

        n = len(word)
        ans = i = 0
        while i < n:
            st = i
            i += 1
            while i < n and abs(ord(word[i]) - ord(word[i - 1])) <= 2:
                i += 1
            ans += f(word[st:i])
        return ans


if __name__ == '__main__':
    # 3
    print(Solution().countCompleteSubstrings("igigee", k=2))
    # 6
    print(Solution().countCompleteSubstrings("aaabbbccc", k=3))
