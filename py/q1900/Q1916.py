"""
 * 你是一只蚂蚁，负责为蚁群构筑 n 间编号从 0 到 n-1 的新房间。
 * 给你一个 下标从 0 开始 且长度为 n 的整数数组 prevRoom 作为扩建计划。
 * 其中，prevRoom[i] 表示在构筑房间 i 之前，你必须先构筑房间 prevRoom[i] ，并且这两个房间必须 直接 相连。
 * 房间 0 已经构筑完成，所以 prevRoom[0] = -1 。
 * 扩建计划中还有一条硬性要求，在完成所有房间的构筑之后，从房间 0 可以访问到每个房间。
 * 你一次只能构筑 一个 房间。
 * 你可以在 已经构筑好的 房间之间自由穿行，只要这些房间是 相连的 。
 * 如果房间 prevRoom[i] 已经构筑完成，那么你就可以构筑房间 i。
 * 返回你构筑所有房间的 不同顺序的数目 。由于答案可能很大，请返回对 109 + 7 取余 的结果。
 * 提示：
 * 1、n == prevRoom.length
 * 2、2 <= n <= 10^5
 * 3、prevRoom[0] == -1
 * 4、对于所有的 1 <= i < n ，都有 0 <= prevRoom[i] < n
 * 5、题目保证所有房间都构筑完成后，从房间 0 可以访问到每个房间
 * 链接：https://leetcode.cn/problems/count-ways-to-build-rooms-in-an-ant-colony/
"""

from functools import cache
import math
from typing import List

#
# @lc app=leetcode.cn id=1916 lang=python3
#
# [1916] 统计为蚁群构筑房间的不同顺序
#


# @lc code=start
class Solution:

    def waysToBuildRooms(self, prevRoom: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(prevRoom)
        g = [[] for _ in range(n)]
        for i in range(1, n):
            g[prevRoom[i]].append(i)

        @cache
        def dfs(idx):  # [子节点数，子方案数]
            if len(g[idx]) == 0:
                return [1, 1]
            ret = [0, 1]
            for nx in g[idx]:
                cnt, sub_ans = dfs(nx)
                ret[0] += cnt
                # 由于每种顺序构建的房间是有序的，将当前的房间加入到已有的房间总数内的顺序数量 = math.comb（房间总数，子房间数）* 子顺序的数量
                ret[1] *= sub_ans * math.comb(ret[0], cnt)
                ret[1] %= MOD
            ret[0] += 1  # 子节点要 +1
            return ret

        return dfs(0)[1]


# @lc code=end

if __name__ == '__main__':
    # 6
    print(Solution().waysToBuildRooms([-1, 0, 0, 1, 2]))
    # 1
    print(Solution().waysToBuildRooms([-1, 0, 1]))
