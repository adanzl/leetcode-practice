"""
 * 给你一个整数 n ，表示有 n 节课，课程编号从 1 到 n 。
 * 同时给你一个二维整数数组 relations ，其中 relations[j] = [prevCourse_j, nextCourse_j] ，
 * 表示课程 prevCourse_j 必须在课程 nextCourse_j 之前 完成（先修课的关系）。
 * 同时给你一个下标从 0 开始的整数数组 time ，其中 time[i] 表示完成第 (i+1) 门课程需要花费的 月份 数。
 * 请你根据以下规则算出完成所有课程所需要的 最少 月份数：
 * 1、如果一门课的所有先修课都已经完成，你可以在 任意 时间开始这门课程。
 * 2、你可以 同时 上 任意门课程 。
 * 请你返回完成所有课程所需要的 最少 月份数。
 * 注意：测试数据保证一定可以完成所有课程（也就是先修课的关系构成一个有向无环图）。
 * 提示：
 * 1、1 <= n <= 5 * 10^4
 * 2、0 <= relations.length <= min(n * (n - 1) / 2, 5 * 10^4)
 * 3、relations[j].length == 2
 * 4、1 <= prevCourse_j, nextCourse_j <= n
 * 5、prevCourse_j != nextCourse_j
 * 6、所有的先修课程对 [prevCourse_j, nextCourse_j] 都是 互不相同 的。
 * 7、time.length == n
 * 8、1 <= time[i] <= 10^4
 * 9、先修课程图是一个有向无环图。
 * 链接：https://leetcode.cn/problems/parallel-courses-iii/
"""
from heapq import heappop, heappush
from typing import List


class Solution:

    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        next_node = [[] for _ in range(n)]
        pre_cnt = [0] * n
        for pc, nc in relations:
            next_node[pc - 1].append(nc - 1)
            pre_cnt[nc - 1] += 1
        q = []
        ans = 0
        for i in range(n):
            if not pre_cnt[i]:
                heappush(q,[time[i], i])
        while q:
            t, idx = heappop(q)
            for nx in next_node[idx]:
                pre_cnt[nx] -= 1
                if not pre_cnt[nx]:
                    heappush(q, [t + time[nx], nx])
            ans = t
        return ans


if __name__ == '__main__':
    # 8
    print(Solution().minimumTime(3, relations=[[1, 3], [2, 3]], time=[3, 2, 5]))
    # 12
    print(Solution().minimumTime(5, relations=[[1, 5], [2, 5], [3, 5], [3, 4], [4, 5]], time=[1, 2, 3, 4, 5]))