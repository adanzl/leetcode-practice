"""
 * 给定一个平衡括号字符串 S，按下述规则计算该字符串的分数：
 * 1、() 得 1 分。
 * 2、AB 得 A + B 分，其中 A 和 B 是平衡括号字符串。
 * 3、(A) 得 2 * A 分，其中 A 是平衡括号字符串。
 * 提示：
 * 1、S 是平衡括号字符串，且只含有 ( 和 ) 。
 * 2、2 <= S.length <= 50
 * 链接：https://leetcode.cn/problems/score-of-parentheses/
"""
from typing import List


class Solution:

    def scoreOfParentheses(self, s: str) -> int:
        n = len(s)
        st = []
        r_dic = dict()
        for i in range(n):
            if s[i] == '(':
                st.append(i)
            else:
                r_dic[st[-1]] = i
                del st[-1]

        def f(l, r):
            if r - l == 1: return 1
            if r_dic[l] == r:
                return 2 * f(l + 1, r - 1)
            i = l
            ret = 0
            while i < r:
                ret += f(i, r_dic[i])
                i = r_dic[i] + 1
            return ret

        return f(0, n - 1)


if __name__ == '__main__':
    # 1
    print(Solution().scoreOfParentheses("()"))
    # 2
    print(Solution().scoreOfParentheses("(())"))
    # 2
    print(Solution().scoreOfParentheses("()()"))
    # 6
    print(Solution().scoreOfParentheses("(()(()))"))