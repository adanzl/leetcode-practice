"""
 * 给你一个字符串 s ，请你判断字符串 s 是否存在一个长度为 2 的子字符串，在其反转后的字符串中也出现。
 * 如果存在这样的子字符串，返回 true; 如果不存在，返回 false 。
 * 提示：
 * 1、1 <= s.length <= 100
 * 2、字符串 s 仅由小写英文字母组成。
 * 链接：https://leetcode.cn/problems/existence-of-a-substring-in-a-string-and-its-reverse/
"""


class Solution:

    def isSubstringPresent(self, s: str) -> bool:
        for i in range(len(s) - 1):
            if s[i:i + 2][::-1] in s:
                return True
        return False


if __name__ == '__main__':
    # True
    print(Solution().isSubstringPresent("leetcode"))
    # True
    print(Solution().isSubstringPresent("abcba"))
    # False
    print(Solution().isSubstringPresent("abcd"))
