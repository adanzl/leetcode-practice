"""
 * 给你一个字符串 word 和一个字符串数组 forbidden 。
 * 如果一个字符串不包含 forbidden 中的任何字符串，我们称这个字符串是 合法 的。
 * 请你返回字符串 word 的一个 最长合法子字符串 的长度。
 * 子字符串 指的是一个字符串中一段连续的字符，它可以为空。
 * 提示：
 * 1、1 <= word.length <= 10^5
 * 2、word 只包含小写英文字母。
 * 3、1 <= forbidden.length <= 10^5
 * 4、1 <= forbidden[i].length <= 10
 * 5、forbidden[i] 只包含小写英文字母。
 * 链接：https://leetcode.cn/problems/length-of-the-longest-valid-substring/
"""
from typing import List


class Solution:

    class TNode:

        def __init__(self):
            self.next = {}
            self.end = False

    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        ans = 0
        tTree = Solution.TNode()
        for w in forbidden:
            p = tTree
            for c in w[::-1]:
                if c not in p.next:
                    p.next[c] = Solution.TNode()
                p = p.next[c]
            p.end = True

        def find(l, r):
            p = tTree
            for i in range(r - 1, l - 1, -1):
                c = word[i]
                if c not in p.next:
                    return False
                if p.next[c].end:
                    return True
                p = p.next[c]
            return p.end

        l, r, n = 0, 0, len(word)
        while r < n:
            while l <= r and find(l, r + 1):
                l += 1
            ans = max(ans, r - l + 1)
            r += 1
        return ans


if __name__ == '__main__':
    # 1
    print(Solution().longestValidSubstring("a", ["n"]))
    # 4
    print(Solution().longestValidSubstring("leetcode", forbidden=["de", "le", "e"]))
    # 4
    print(Solution().longestValidSubstring("cbaaaabc", forbidden=["aaa", "cb"]))