"""
 * 你总共需要上 numCourses 门课，课程编号依次为 0 到 numCourses-1 。你会得到一个数组 prerequisite ，其中 prerequisites[i] = [ai, bi] 表示如果你想选 bi 课程，你 必须 先选 ai 课程。
 * 有的课会有直接的先修课程，比如如果想上课程 1 ，你必须先上课程 0 ，那么会以 [0,1] 数对的形式给出先修课程数对。
 * 先决条件也可以是 间接 的。如果课程 a 是课程 b 的先决条件，课程 b 是课程 c 的先决条件，那么课程 a 就是课程 c 的先决条件。
 * 你也得到一个数组 queries ，其中 queries[j] = [uj, vj]。对于第 j 个查询，您应该回答课程 uj 是否是课程 vj 的先决条件。
 * 返回一个布尔数组 answer ，其中 answer[j] 是第 j 个查询的答案。
 * 提示：
 * 1、2 <= numCourses <= 100
 * 2、0 <= prerequisites.length <= (numCourses * (numCourses - 1) / 2)
 * 3、prerequisites[i].length == 2
 * 4、0 <= ai, bi <= n - 1
 * 5、ai != bi
 * 6、每一对 [ai, bi] 都 不同
 * 7、先修课程图中没有环。
 * 8、1 <= queries.length <= 10^4
 * 9、0 <= ui, vi <= n - 1
 * 10、ui != vi
 * 链接：https://leetcode.cn/problems/course-schedule-iv
"""
from typing import List
#
# @lc app=leetcode.cn id=1462 lang=python3
#
# [1462] 构造字符串的总得分和
#

# @lc code=start


class Solution:

    def checkIfPrerequisite(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[bool]:
        pre = [0 for _ in range(n)]
        nxt = [[] for _ in range(n)]
        pre_set = [set() for _ in range(n)]

        # 拓扑排序
        for a, b in edges:
            pre[b] += 1
            nxt[a].append(b)
            pre_set[b].add(a)
        depth = [-1] * n
        end_node = [v for v in range(n) if pre[v] == 0]
        deep, idx, end = 0, 0, len(end_node)
        while end_node:
            if idx == end:
                deep += 1
                end += len(end_node)
            v = end_node.pop(0)
            depth[v] = deep + 1
            for nx in nxt[v]:
                pre_set[nx].update(pre_set[v])
                pre[nx] -= 1
                if pre[nx] == 0:
                    end_node.append(nx)
            idx += 1

        ans = [False] * len(queries)
        for i, (u, v) in enumerate(queries):
            if u in pre_set[v]:
                ans[i] = True
        return ans


# @lc code=end

if __name__ == '__main__':
    # [false,true]
    print(Solution().checkIfPrerequisite(2, edges=[[1, 0]], queries=[[0, 1], [1, 0]]))
    # [false,false]
    print(Solution().checkIfPrerequisite(2, edges=[], queries=[[1, 0], [0, 1]]))
    # [true,true]
    print(Solution().checkIfPrerequisite(3, edges=[[1, 2], [1, 0], [2, 0]], queries=[[1, 0], [1, 2]]))
