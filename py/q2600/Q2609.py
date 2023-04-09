"""
 * 给你一个仅由 0 和 1 组成的二进制字符串 s 。  
 * 如果子字符串中 所有的 0 都在 1 之前 且其中 0 的数量等于 1 的数量，则认为 s 的这个子字符串是平衡子字符串。请注意，空子字符串也视作平衡子字符串。 
 * 返回  s 中最长的平衡子字符串长度。
 * 子字符串是字符串中的一个连续字符序列。
 * 提示：
 * 1、1 <= s.length <= 50
 * 2、'0' <= s[i] <= '1'
 * 链接：https://leetcode.cn/problems/find-the-longest-balanced-substring-of-a-binary-string/
"""


class Solution:

    def findTheLongestBalancedSubstring(self, s: str) -> int:
        ans = 0
        c0, c1 = 0, 0
        for c in s:
            if c == '0':
                if c1: c0 = 0
                c0 += 1
                c1 = 0
            else:
                c1 += 1
            ans = max(ans, min(c0, c1) * 2)
        return ans


if __name__ == '__main__':
    # 6
    print(Solution().findTheLongestBalancedSubstring("01000111"))
    # 4
    print(Solution().findTheLongestBalancedSubstring("00111"))
    # 0
    print(Solution().findTheLongestBalancedSubstring("111"))
