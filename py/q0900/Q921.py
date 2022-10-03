"""
 * 只有满足下面几点之一，括号字符串才是有效的：
 * 1、它是一个空字符串，或者
 * 2、它可以被写成 AB （A 与 B 连接）, 其中 A 和 B 都是有效字符串，或者
 * 3、它可以被写作 (A)，其中 A 是有效字符串。
 * 给定一个括号字符串 s ，移动N次，你就可以在字符串的任何位置插入一个括号。
 * 例如，如果 s = "()))" ，你可以插入一个开始括号为 "(()))" 或结束括号为 "())))" 。
 * 返回 为使结果字符串 s 有效而必须添加的最少括号数。
 * 提示：
 * 1、1 <= s.length <= 1000
 * 2、s 只包含 '(' 和 ')' 字符。
 * 链接：https://leetcode.cn/problems/minimum-add-to-make-parentheses-valid/
"""


class Solution:

    def minAddToMakeValid(self, s: str) -> int:
        ans, pre = 0, 0
        for c in s:
            if c == '(':
                pre += 1
            else:
                pre -= 1
            if pre < 0:
                ans += 1
            pre = max(pre, 0)
        return ans + pre


if __name__ == '__main__':
    # 1
    print(Solution().minAddToMakeValid("())"))
    # 3
    print(Solution().minAddToMakeValid("((("))