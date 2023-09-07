"""
 * 游戏中存在两种角色：
 * 1、好人：该角色只说真话。
 * 2、坏人：该角色可能说真话，也可能说假话。
 * 给你一个下标从 0 开始的二维整数数组 statements ，大小为 n x n ，表示 n 个玩家对彼此角色的陈述。
 * 具体来说，statements[i][j] 可以是下述值之一：
 * 1、0 表示 i 的陈述认为 j 是 坏人 。
 * 2、1 表示 i 的陈述认为 j 是 好人 。
 * 3、2 表示 i 没有对 j 作出陈述。
 * 另外，玩家不会对自己进行陈述。形式上，对所有 0 <= i < n ，都有 statements[i][i] = 2 。
 * 根据这 n 个玩家的陈述，返回可以认为是 好人 的 最大 数目。
 * 提示：
 * 1、n == statements.length == statements[i].length
 * 2、2 <= n <= 15
 * 3、statements[i][j] 的值为 0、1 或 2
 * 4、statements[i][i] == 2
 * 链接：https://leetcode.cn/problems/maximum-good-people-based-on-statements/
"""

from typing import List

#
# @lc app=leetcode.cn id=2151 lang=python3
#
# [2151] 基于陈述统计最多好人数
#


# @lc code=start
class Solution:

    def maximumGood(self, statements: List[List[int]]) -> int:
        n = len(statements)

        def check(f):  # 0: bad, 1: good
            for i in range(n):
                if f & (1 << i) == 0: continue
                for j in range(n):
                    if statements[i][j] == 2: continue
                    if statements[i][j] != ((f >> j) & 1):
                        return False
            return True

        ans = 0
        for i in range(1 << n):
            if check(i):
                ans = max(ans, i.bit_count())
        return ans


# @lc code=end

if __name__ == '__main__':
    # 2
    print(Solution().maximumGood([[2, 1, 2], [1, 2, 2], [2, 0, 2]]))
    # 1
    print(Solution().maximumGood([[2, 0], [0, 2]]))
