"""
 * 给你一个 n 个节点的带权无向图，节点编号为 0 到 n - 1 。
 * 给你一个整数 n 和一个数组 edges ，其中 edges[i] = [u_i, v_i, w_i] 表示节点 u_i 和 v_i 之间有一条权值为 w_i 的无向边。
 * 在图中，一趟旅途包含一系列节点和边。旅途开始和结束点都是图中的节点，且图中存在连接旅途中相邻节点的边。
 * 注意，一趟旅途可能访问同一条边或者同一个节点多次。
 * 如果旅途开始于节点 u ，结束于节点 v ，我们定义这一趟旅途的 代价 是经过的边权按位与 AND 的结果。
 * 换句话说，如果经过的边对应的边权为 w_0, w_1, w_2, ..., w_k ，那么代价为w_0 & w_1 & w_2 & ... & w_k ，其中 & 表示按位与 AND 操作。
 * 给你一个二维数组 query ，其中 query[i] = [s_i, t_i] 。
 * 对于每一个查询，你需要找出从节点开始 s_i ，在节点 t_i 处结束的旅途的最小代价。
 * 如果不存在这样的旅途，答案为 -1 。
 * 返回数组 answer ，其中 answer[i] 表示对于查询 i 的 最小 旅途代价。
 * 提示：
 * 1、1 <= n <= 10^5
 * 2、0 <= edges.length <= 10^5
 * 3、edges[i].length == 3
 * 4、0 <= u_i, v_i <= n - 1
 * 5、u_i != v_i
 * 6、0 <= w_i <= 10^5
 * 7、1 <= query.length <= 10^5
 * 8、query[i].length == 2
 * 9、0 <= s_i, t_i <= n - 1
 * 链接：https://leetcode.cn/contest/weekly-contest-392/problems/minimum-cost-walk-in-weighted-graph/
"""
from typing import List


class Solution:

    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        parent = [i for i in range(n)]

        values = [(1 << 20) - 1] * n

        def find(x):
            if x == parent[x]: return x
            parent[x] = find(parent[x])
            return parent[x]

        for u, v, w in edges:
            r0, r1 = find(u), find(v)
            parent[r1] = parent[r0]
            values[r0] &= w
            values[r0] &= values[r1]
        ans = []
        for s, t in query:
            if s == t:
                ans.append(0)
            else:
                r0, r1 = find(s), find(t)
                if r0 != r1:
                    ans.append(-1)
                else:
                    ans.append(values[r0])
        return ans


if __name__ == '__main__':
    # [0,0,0]
    print(Solution().minimumCost(
        10, [[9, 7, 9], [8, 3, 7], [7, 0, 11], [6, 3, 8], [6, 1, 3], [7, 3, 0], [2, 3, 9], [8, 9, 12]],
        [[0, 6], [1, 0], [2, 9]]))
    # [7,1,-1,0,-1,-1,0,-1]
    print(Solution().minimumCost(9, [[0, 4, 7], [3, 5, 1], [1, 3, 5], [1, 5, 1]],
                                 [[0, 4], [1, 5], [3, 0], [3, 3], [3, 2], [2, 0], [7, 7], [7, 0]]))
    # [1,-1]
    print(Solution().minimumCost(5, edges=[[0, 1, 7], [1, 3, 7], [1, 2, 1]], query=[[0, 3], [3, 4]]))
    # [0]
    print(Solution().minimumCost(3, edges=[[0, 2, 7], [0, 1, 15], [1, 2, 6], [1, 2, 1]], query=[[1, 2]]))
