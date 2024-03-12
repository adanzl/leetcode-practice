"""
 * 给你一个下标从 0 开始的字符串数组 words 。
 * 定义一个 布尔 函数 isPrefixAndSuffix ，它接受两个字符串参数 str1 和 str2 ：
 * 当 str1 同时是 str2 的前缀（prefix）和后缀（suffix）时，isPrefixAndSuffix(str1, str2) 返回 true，否则返回 false。
 * 例如，isPrefixAndSuffix("aba", "ababa") 返回 true，因为 "aba" 既是 "ababa" 的前缀，也是 "ababa" 的后缀，
 * 但是 isPrefixAndSuffix("abc", "abcd") 返回 false。
 * 以整数形式，返回满足 i < j 且 isPrefixAndSuffix(words[i], words[j]) 为 true 的下标对 (i, j) 的 数量 。
 * 提示：
 * 1、1 <= words.length <= 10^5
 * 2、1 <= words[i].length <= 10^5
 * 3、words[i] 仅由小写英文字母组成。
 * 4、所有 words[i] 的长度之和不超过 5 * 10^5 。
 * 链接：https://leetcode.cn/problems/count-prefix-and-suffix-pairs-i/description/
"""
from typing import Counter, List


class Solution:

    def countPrefixSuffixPairs(self, words: List[str]) -> int:

        def get_z(s):
            l = r = 0
            n = len(s)
            z = [0] * n
            z[0] = n
            for i in range(1, n):
                if i <= r:
                    z[i] = min(r - i + 1, z[i - l])
                while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                    z[i] += 1
                if i + z[i] - 1 > r:
                    l = i
                    r = i + z[i] - 1
            return z

        ans = 0
        cnt = Counter()
        for word in words:
            z = get_z(word)
            n = len(word)
            for i, v in enumerate(z):
                if v == n - i:
                    ans += cnt[word[:v]]
            cnt[word] += 1
        return ans


if __name__ == '__main__':
    # 0
    print(Solution().countPrefixSuffixPairs(["a", "abb"]))
    # 4
    print(Solution().countPrefixSuffixPairs(["a", "aba", "ababa", "aa"]))
    # 2
    print(Solution().countPrefixSuffixPairs(["pa", "papa", "ma", "mama"]))
    # 0
    print(Solution().countPrefixSuffixPairs(["abab", "ab"]))
