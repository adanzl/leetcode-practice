"""
 * 给你一个字符串 s 。它可能包含任意数量的 '*' 字符。你的任务是删除所有的 '*' 字符。
 * 当字符串还存在至少一个 '*' 字符时，你可以执行以下操作：
 * 删除最左边的 '*' 字符，同时删除该星号字符左边一个字典序 最小 的字符。如果有多个字典序最小的字符，你可以删除它们中的任意一个。
 * 请你返回删除所有 '*' 字符以后，剩余字符连接而成的 字典序最小 的字符串。
 * 提示：
 * 1、1 <= s.length <= 10^5
 * 2、s 只含有小写英文字母和 '*' 字符。
 * 3、输入保证操作可以删除所有的 '*' 字符。
 * 链接：https://leetcode.cn/problems/lexicographically-minimum-string-after-removing-stars/
"""
from heapq import heappop, heappush


class Solution:

    def clearStars(self, s: str) -> str:
        h = []
        for i, c in enumerate(s):
            if c == '*':
                heappop(h)
            else:
                heappush(h, [c, -i])
        return ''.join([s[-v[1]] for v in sorted(h, key=lambda x: -x[1])])


if __name__ == '__main__':
    # "aab"
    print(Solution().clearStars("aaba*"))
    # "abc"
    print(Solution().clearStars("abc"))
