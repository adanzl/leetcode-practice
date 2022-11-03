"""
 * 给你一个字符串数组 words 。words 中每个元素都是一个包含 两个 小写英文字母的单词。
 * 请你从 words 中选择一些元素并按 任意顺序 连接它们，并得到一个 尽可能长的回文串 。每个元素 至多 只能使用一次。
 * 请你返回你能得到的最长回文串的 长度 。如果没办法得到任何一个回文串，请你返回 0 。
 * 回文串 指的是从前往后和从后往前读一样的字符串。
 * 提示：
 * 1、1 <= words.length <= 10^5
 * 2、words[i].length == 2
 * 3、words[i] 仅包含小写英文字母。
 * 链接：https://leetcode.cn/problems/longest-palindrome-by-concatenating-two-letter-words/
"""
from typing import Counter, List


class Solution:

    def longestPalindrome(self, words: List[str]) -> int:
        cnt = Counter(words)
        ans = 0
        mxr = 0
        for w, c in cnt.items():
            rw = w[::-1]
            if w == rw:
                ans += (c & ~1) * len(w)
                if c % 2: mxr = max(mxr, len(w))
            else:
                ans += min(cnt[w], cnt[rw]) * len(w)
        return ans + mxr


if __name__ == '__main__':
    # 22
    print(Solution().longestPalindrome(["dd", "aa", "bb", "dd", "aa", "dd", "bb", "dd", "aa", "cc", "bb", "cc", "dd", "cc"]))
    # 6
    print(Solution().longestPalindrome(["lc", "cl", "gg"]))
    # 8
    print(Solution().longestPalindrome(["ab", "ty", "yt", "lc", "cl", "ab"]))
    # 2
    print(Solution().longestPalindrome(["cc", "ll", "xx"]))
