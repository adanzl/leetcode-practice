"""
 * 给你一个字符串 s ，请你判断它是否 有效 。
 * 字符串 s 有效 需要满足：假设开始有一个空字符串 t = "" ，你可以执行 任意次 下述操作将 t 转换为 s ：
 * 将字符串 "abc" 插入到 t 中的任意位置。形式上，t 变为 t_left + "abc" + t_right，其中 t == t_left + t_right 。
 * 注意，t_left 和 t_right 可能为 空 。
 * 如果字符串 s 有效，则返回 true; 否则，返回 false。
 * 提示：
 * 1、1 <= s.length <= 2 * 10^4
 * 2、s 由字母 'a'、'b' 和 'c' 组成
 * 链接：https://leetcode.cn/problems/check-if-word-is-valid-after-substitutions/
"""


class Solution:

    def isValid(self, s: str) -> bool:
        while s and 'abc' in s:
            s = s.replace('abc', '')
        return s == ''


if __name__ == '__main__':
    # True
    print(Solution().isValid("aabcbc"))
    # True
    print(Solution().isValid("abcabcababcc"))
    # False
    print(Solution().isValid("abccba"))
