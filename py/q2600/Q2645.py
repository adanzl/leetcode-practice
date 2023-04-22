"""
 * 给你一个字符串 word ，你可以向其中任何位置插入 "a"、"b" 或 "c" 任意次，返回使 word 有效 需要插入的最少字母数。
 * 如果字符串可以由 "abc" 串联多次得到，则认为该字符串 有效 。     
 * 提示：
 * 1、1 <= word.length <= 50
 * 2、word 仅由字母 "a"、"b" 和 "c" 组成。
 * 链接：https://leetcode.cn/problems/minimum-additions-to-make-valid-string/
"""


class Solution:

    def addMinimum(self, word: str) -> int:
        ans = 0
        pre = 'c'
        for c in word:
            if c == 'a':
                if pre == 'b':
                    ans += 1
                elif pre == 'a':
                    ans += 2
            elif c == 'b':
                if pre == 'c':
                    ans += 1
                elif pre == 'b':
                    ans += 2
            elif c == 'c':
                if pre == 'a':
                    ans += 1
                elif pre == 'c':
                    ans += 2
            pre = c
        if pre == 'a':
            ans += 2
        elif pre == 'b':
            ans += 1
        return ans


if __name__ == '__main__':
    # 9
    print(Solution().addMinimum("aaaabb"))
    # 2
    print(Solution().addMinimum("b"))
    # 6
    print(Solution().addMinimum("aaa"))
    # 0
    print(Solution().addMinimum("abc"))
