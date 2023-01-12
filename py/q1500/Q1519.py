"""
 * 给你一棵树（即，一个连通的无环无向图），这棵树由编号从 0  到 n - 1 的 n 个节点组成，且恰好有 n - 1 条 edges 。
 * 树的根节点为节点 0 ，树上的每一个节点都有一个标签，也就是字符串 labels 中的一个小写字符（编号为 i 的 节点的标签就是 labels[i] ）
 * 边数组 edges 以 edges[i] = [ai, bi] 的形式给出，该格式表示节点 ai 和 bi 之间存在一条边。
 * 返回一个大小为 n 的数组，其中 ans[i] 表示第 i 个节点的子树中与节点 i 标签相同的节点数。
 * 树 T 中的子树是由 T 中的某个节点及其所有后代节点组成的树。
 * 提示：
 * 1、1 <= n <= 10^5
 * 2、edges.length == n - 1
 * 3、edges[i].length == 2
 * 4、0 <= ai, bi < n
 * 5、ai != bi
 * 6、labels.length == n
 * 7、labels 仅由小写英文字母组成
 * 链接：https://leetcode.cn/problems/number-of-nodes-in-the-sub-tree-with-the-same-label/
"""
from typing import Counter, List


class Solution:

    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        ans = [0] * n
        g = [[] for _ in range(n)]
        for s, e in edges:
            g[s].append(e)
            g[e].append(s)

        def dfs(idx, fa):
            ret = Counter()
            for nx in g[idx]:
                if nx == fa: continue
                ret += dfs(nx, idx)
            ret[labels[idx]] += 1
            ans[idx] = ret[labels[idx]]
            return ret
        dfs(0, -1)
        return ans


if __name__ == '__main__':
    # [2,1,1,1,1,1,1]
    print(Solution().countSubTrees(7, edges=[[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]], labels="abaedcd"))
    # [4,2,1,1]
    print(Solution().countSubTrees(4, edges=[[0, 1], [1, 2], [0, 3]], labels="bbbb"))
    # [3,2,1,1,1]
    print(Solution().countSubTrees(5, edges=[[0, 1], [0, 2], [1, 3], [0, 4]], labels="aabab"))
    #
    # print(Solution().countSubTrees())