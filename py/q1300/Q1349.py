"""
 * 给你一个 m * n 的矩阵 seats 表示教室中的座位分布。如果座位是坏的（不可用），就用 '#' 表示；否则，用 '.' 表示。
 * 学生可以看到左侧、右侧、左上、右上这四个方向上紧邻他的学生的答卷，但是看不到直接坐在他前面或者后面的学生的答卷。
 * 请你计算并返回该考场可以容纳的一起参加考试且无法作弊的最大学生人数。
 * 学生必须坐在状况良好的座位上。
 * 提示：
 * 1、seats 只包含字符 '.' 和'#'
 * 2、m == seats.length
 * 3、n == seats[i].length
 * 4、1 <= m <= 8
 * 5、1 <= n <= 8
 * 链接：https://leetcode.cn/problems/maximum-students-taking-exam/
"""
from functools import reduce
from operator import or_
from typing import List


class Solution:
    # 状态压缩 数位表示坐位状态
    def maxStudents(self, seats: List[List[str]]) -> int:
        m, n = len(seats), len(seats[0])
        masks = [reduce(or_, [(1 << i if seats[_][i] == '#' else 0) for i in range(n)]) for _ in range(m)]
        dp = [0] * (1 << n)
        for i in range(m):
            ndp = [0] * (1 << n)
            for state in range(1 << n):
                if state & masks[i] != 0: continue  # 校验是否是坏椅子
                if any([1 << j & state and 1 << (j + 1) & state for j in range(n - 1)]): continue  # 校验是否左右连坐
                for j in range(1 << n):
                    if j & (state << 1) or j & (state >> 1): continue  # 校验是否可以从该状态迁移过来
                    ndp[state] = max(ndp[state], dp[j] + state.bit_count())
            dp = ndp
        return max(dp)


if __name__ == '__main__':
    # 4
    print(Solution().maxStudents([["#", ".", "#", "#", ".", "#"], [".", "#", "#", "#", "#", "."], ["#", ".", "#", "#", ".", "#"]]))
    # 3
    print(Solution().maxStudents([[".", "#"], ["#", "#"], ["#", "."], ["#", "#"], [".", "#"]]))
    # 10
    print(Solution().maxStudents([["#", ".", ".", ".", "#"], [".", "#", ".", "#", "."], [".", ".", "#", ".", "."], [".", "#", ".", "#", "."], ["#", ".", ".", ".", "#"]]))
