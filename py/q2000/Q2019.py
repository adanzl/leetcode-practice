"""
 * 给你一个字符串 s ，它 只 包含数字 0-9 ，加法运算符 '+' 和乘法运算符 '*' ，
 * 这个字符串表示一个 合法 的只含有 个位数数字 的数学表达式（比方说 3+5*2）。
 * 有 n 位小学生将计算这个数学表达式，并遵循如下 运算顺序 ：
 * 1、按照 从左到右 的顺序计算 乘法 ，然后
 * 2、按照 从左到右 的顺序计算 加法 。
 * 给你一个长度为 n 的整数数组 answers ，表示每位学生提交的答案。你的任务是给 answer 数组按照如下 规则 打分：
 * 1、如果一位学生的答案 等于 表达式的正确结果，这位学生将得到 5 分。
 * 2、否则，如果答案由 一处或多处错误的运算顺序 计算得到，那么这位学生能得到 2 分。
 * 3、否则，这位学生将得到 0 分。
 * 请你返回所有学生的分数和。
 * 提示：
 * 1、3 <= s.length <= 31
 * 2、s 表示一个只包含 0-9 ，'+' 和 '*' 的合法表达式。
 * 3、表达式中所有整数运算数字都在闭区间 [0, 9] 以内。
 * 4、1 <= 数学表达式中所有运算符数目（'+' 和 '*'） <= 15
 * 5、测试数据保证正确表达式结果在范围 [0, 1000] 以内。
 * 6、n == answers.length
 * 7、1 <= n <= 10^4
 * 8、0 <= answers[i] <= 1000
 * 链接：https://leetcode.cn/problems/the-score-of-students-solving-math-expression/
"""

from functools import cache
from itertools import product
from typing import List

#
# @lc app=leetcode.cn id=2019 lang=python3
#
# [2019] 解出数学表达式的学生分数
#


# @lc code=start
class Solution:

    def scoreOfStudents(self, s: str, answers: List[int]) -> int:

        @cache
        def dfs(l, r):
            if l == r:
                return set([int(s[l])])
            ret = set()
            for i in range(l + 1, r, 2):
                vs0 = dfs(l, i - 1)
                vs1 = dfs(i + 1, r)
                for v0, v1 in product(vs0, vs1):
                    vv = (v0 + v1) if s[i] == '+' else (v0 * v1)
                    if vv <= 1000:
                        ret.add(vv)
            return ret

        ss = dfs(0, len(s) - 1)
        q = []
        op = '+'
        for c in s:
            if c.isdigit():
                v = int(c)
                if op == '*':
                    v *= q.pop()
                q.append(v)
            else:
                op = c
        valid_ans = sum(q)
        ss.discard(valid_ans)
        ans = 0
        for a in answers:
            if a in ss:
                ans += 2
            if a == valid_ans:
                ans += 5
        return ans


# @lc code=end

if __name__ == '__main__':
    # 6
    print(Solution().scoreOfStudents("2+6*1+1+2*0+1+3*4+4*0+0*3+3*6+0", answers=[20, 13, 42]))
    # 7
    print(Solution().scoreOfStudents("7+3*1*2", answers=[20, 13, 42]))
    # 19
    print(Solution().scoreOfStudents("3+5*2", answers=[13, 0, 10, 13, 13, 16, 16]))
    # 10
    print(Solution().scoreOfStudents("6+0*1", answers=[12, 9, 6, 4, 8, 6]))
