"""
 * 给你两个字符串 s1 和 s2 ，两个字符串的长度都为 4 ，且只包含 小写 英文字母。
 * 你可以对两个字符串中的 任意一个 执行以下操作 任意 次：
 * 选择两个下标 i 和 j 且满足 j - i = 2 ，然后 交换 这个字符串中两个下标对应的字符。
 * 如果你可以让字符串 s1 和 s2 相等，那么返回 true ，否则返回 false 。
 * 提示：
 * 1、s1.length == s2.length == 4
 * 2、s1 和 s2 只包含小写英文字母。
 * 链接：https://leetcode.cn/problems/check-if-strings-can-be-made-equal-with-operations-i/
"""


class Solution:

    def canBeEqual(self, s1: str, s2: str) -> bool:
        return sorted([s1[0], s1[2]]) == sorted([s2[0], s2[2]]) and sorted([s1[1], s1[3]]) == sorted([s2[1], s2[3]])


if __name__ == '__main__':
    # true
    print(Solution().canBeEqual("abcd", s2="cdab"))
    # false
    print(Solution().canBeEqual("abcd", s2="dacb"))