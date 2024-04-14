"""
 * 给你一个字符串 s 。一个字符串的 分数 定义为相邻字符 ASCII 码差值绝对值的和。
 * 请你返回 s 的 分数 。
 * 提示：
 * 1、2 <= s.length <= 100
 * 2、s 只包含小写英文字母。
 * 链接：https://leetcode.cn/problems/score-of-a-string/
"""
from itertools import pairwise


class Solution:

    def scoreOfString(self, s: str) -> int:
        ans = 0
        for c0, c1 in pairwise(s):
            ans += abs(ord(c0) - ord(c1))
        return ans


if __name__ == '__main__':
    # 13
    print(Solution().scoreOfString('hello'))
    # 50
    print(Solution().scoreOfString('zaz'))
