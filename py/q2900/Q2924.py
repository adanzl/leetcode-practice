"""
 * 一场比赛中共有 n 支队伍，按从 0 到  n - 1 编号。每支队伍也是 有向无环图（DAG） 上的一个节点。
 * 给你一个整数 n 和一个下标从 0 开始、长度为 m 的二维整数数组 edges 表示这个有向无环图，
 * 其中 edges[i] = [ui, vi] 表示图中存在一条从 ui 队到 vi 队的有向边。
 * 从 a 队到 b 队的有向边意味着 a 队比 b 队 强 ，也就是 b 队比 a 队 弱 。
 * 在这场比赛中，如果不存在某支强于 a 队的队伍，则认为 a 队将会是 冠军 。
 * 如果这场比赛存在 唯一 一个冠军，则返回将会成为冠军的队伍。否则，返回 -1 。
 * 注意
 * 环 是形如 a1, a2, ..., an, an+1 的一个序列，且满足：节点 a1 与节点 an+1 是同一个节点；节点 a1, a2, ..., an 互不相同；
 * 对于范围 [1, n] 中的每个 i ，均存在一条从节点 ai 到节点 ai+1 的有向边。
 * 有向无环图 是不存在任何环的有向图。
 * 提示：
 * 1、1 <= n <= 100
 * 2、m == edges.length
 * 3、0 <= m <= n * (n - 1) / 2
 * 4、edges[i].length == 2
 * 5、0 <= edge[i][j] <= n - 1
 * 6、edges[i][0] != edges[i][1]
 * 7、生成的输入满足：如果 a 队比 b 队强，就不存在 b 队比 a 队强
 * 8、生成的输入满足：如果 a 队比 b 队强，b 队比 c 队强，那么 a 队比 c 队强
 * 链接：https://leetcode.cn/problems/find-champion-ii/
"""
from typing import List


class Solution:

    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        ss = set([i for i in range(n)])
        for u, v in edges:
            ss.discard(v)
        return -1 if len(ss) != 1 else list(ss)[0]


if __name__ == '__main__':
    # 0
    print(Solution().findChampion(3, edges=[[0, 1], [1, 2]]))
    # -1
    print(Solution().findChampion(4, edges=[[0, 2], [1, 3], [1, 2]]))
