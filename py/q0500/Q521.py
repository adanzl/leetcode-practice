"""
 * 给你两个字符串 a 和 b，请返回 这两个字符串中 最长的特殊序列  的长度。如果不存在，则返回 -1 。
 * 「最长特殊序列」 定义如下：该序列为 某字符串独有的最长 子序列（即不能是其他字符串的子序列） 。
 * 字符串 s 的子序列是在从 s 中删除任意数量的字符后可以获得的字符串。
 * 例如，"abc" 是 "aebdc" 的子序列，因为删除 "aebdc" 中斜体加粗的字符可以得到 "abc" 。 
 * "aebdc" 的子序列还包括 "aebdc" 、 "aeb" 和 "" (空字符串)。
 * 提示：
 * 1、1 <= a.length, b.length <= 100
 * 2、a 和 b 由小写英文字母组成
 * 链接：https://leetcode.cn/problems/longest-uncommon-subsequence-i
"""


class Solution:

    def findLUSlength(self, a: str, b: str) -> int:
        if a != b:
            return max(len(a), len(b))
        ans = -1
        for c in a:
            if c not in b:
                ans = max(ans, len(a))
        for c in b:
            if c not in a:
                ans = max(ans, len(b))
        return ans


if __name__ == '__main__':
    # 17
    print(Solution().findLUSlength("aefawfawfawfaw", "aefawfeawfwafwaef"))
    # 7
    print(Solution().findLUSlength("aaaabcd", "aaaaacd"))
    # 3
    print(Solution().findLUSlength("aba", b="cdc"))
    # 3
    print(Solution().findLUSlength("aaa", b="bbb"))
    # -1
    print(Solution().findLUSlength("aaa", b="aaa"))
