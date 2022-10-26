"""
 * 你会得到一个字符串 text 。你应该把它分成 k 个子字符串 (subtext_1, subtext_2，…， subtext_k) ，要求满足:
 * 1、subtext_i 是 非空 字符串
 * 2、所有子字符串的连接等于 text ( 即subtext_1 + subtext_2 + ... + subtext_k == text )
 * 1、subtext_i == subtext_k - i + 1 表示所有 i 的有效值( 即 1 <= i <= k )
 * 返回k可能最大值。
 * 提示：
 * 1、1 <= text.length <= 1000
 * 2、text 仅由小写英文字符组成
 * 链接：https://leetcode.cn/problems/longest-chunked-palindrome-decomposition/
"""
from typing import List


class Solution:

    def longestDecomposition(self, text: str) -> int:
        n = len(text)
        l = n // 2
        dp = [1] * (l + 1)
        ext = 0 if n % 2 == 0 else 1
        dp[0] = ext
        for i in range(l):
            for j in range(i + 1):  # sub str len is j
                if text[l - i - 1:l - i + j] == text[ext + l + i - j:ext + l + i + 1]:
                    dp[i + 1] = max(dp[i + 1], dp[i - j] + 2)
        return dp[-1]


if __name__ == '__main__':
    # 11
    print(Solution().longestDecomposition("antaprezatepzapreanta"))
    # 7
    print(Solution().longestDecomposition("ghiabcdefhelloadamhelloabcdefghi"))
    # 1
    print(Solution().longestDecomposition("merchant"))