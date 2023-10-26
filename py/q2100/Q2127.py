"""
 * 一个公司准备组织一场会议，邀请名单上有 n 位员工。公司准备了一张 圆形 的桌子，可以坐下 任意数目 的员工。
 * 员工编号为 0 到 n - 1 。每位员工都有一位 喜欢 的员工，每位员工 当且仅当 他被安排在喜欢员工的旁边，他才会参加会议。
 * 每位员工喜欢的员工 不会 是他自己。
 * 给你一个下标从 0 开始的整数数组 favorite ，其中 favorite[i] 表示第 i 位员工喜欢的员工。请你返回参加会议的 最多员工数目 。
 * 提示：
 * 1、n == favorite.length
 * 2、2 <= n <= 10^5
 * 3、0 <= favorite[i] <= n - 1
 * 4、favorite[i] != i
 * 链接：https://leetcode.cn/problems/maximum-employees-to-be-invited-to-a-meeting/
"""

from typing import Deque, List

#
# @lc app=leetcode.cn id=2127 lang=python3
#
# [2127] 参加会议的最多员工数
#


# @lc code=start
class Solution:

    def maximumInvitations(self, favorite: List[int]) -> int:
        # 基数环
        n = len(favorite)
        income = [0] * n  # 入度
        nxt = [[] for _ in range(n)]
        link = [1] * n  # 单链长度
        for i, f in enumerate(favorite):
            nxt[i].append(f)
            income[f] += 1
        q = Deque([i for i in range(n) if income[i] == 0])
        vis = [False] * n
        while q:  # 拓扑排序 去除单链
            i = q.popleft()
            vis[i] = True
            for nx in nxt[i]:
                income[nx] -= 1
                link[nx] = link[i] + 1
                if income[nx] == 0:
                    q.append(nx)
        # dfs 确定环长度 return 环长度,环终点
        def dfs(i, ln):
            vis[i] = True
            for nx in nxt[i]:
                if vis[nx]: continue
                return dfs(nx, ln + 1)
            return ln, i

        ans, ln_2 = 0, 0
        for i in range(n):
            if vis[i]: continue
            ln, end = dfs(i, 1)
            ans = max(ans, ln)
            if ln == 2:
                ln_2 += link[end] + link[i]
        # case_1：一个环 size > 2
        # case_2：所有长度为2的环的和 加上 与size为2的环的最长链的总和
        return max(ans, ln_2)


# @lc code=end

if __name__ == '__main__':
    # 3
    print(Solution().maximumInvitations([2, 2, 1, 2]))
    # 4
    print(Solution().maximumInvitations([3, 0, 1, 4, 1]))
    # 3
    print(Solution().maximumInvitations([1, 2, 0]))
