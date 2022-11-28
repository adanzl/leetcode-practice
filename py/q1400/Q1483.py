"""
 * 给你一棵树，树上有 n 个节点，按从 0 到 n-1 编号。树以父节点数组的形式给出，其中 parent[i] 是节点 i 的父节点。树的根节点是编号为 0 的节点。
 * 树节点的第 k 个祖先节点是从该节点到根节点路径上的第 k 个节点。
 * 实现 TreeAncestor 类：
 * 1、TreeAncestor（int n， int[] parent） 对树和父数组中的节点数初始化对象。
 * 2、getKthAncestor(int node, int k) 返回节点 node 的第 k 个祖先节点。如果不存在这样的祖先节点，返回 -1 。
 * 提示：
 * 1、1 <= k <= n <= 5 * 10^4
 * 2、parent[0] == -1 表示编号为 0 的节点是根节点。
 * 3、对于所有的 0 < i < n ，0 <= parent[i] < n 总成立
 * 4、0 <= node < n
 * 5、至多查询 5 * 10^4 次
 * 链接：https://leetcode.cn/problems/kth-ancestor-of-a-tree-node/
"""
from typing import List


class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        # Binary Lifting
        self.parent = [[parent[i]] for i in range(n)]  # num-指数
        for i in range(1, 16 + 1):  #  最大2^16
            for j in range(n):  # num
                if len(self.parent[j]) <= i - 1: continue
                pre = self.parent[j][i - 1]
                if pre != -1 and len(self.parent[pre]) >= i:
                    self.parent[j].append(self.parent[pre][i - 1])

    def getKthAncestor(self, node: int, k: int) -> int:
        if node == -1: return -1
        if k == 0: return node
        low_bit = k & (-k)
        pos = low_bit.bit_length() - 1  # 查询右侧第一个1的位置
        if len(self.parent[node]) <= pos: return -1
        return self.getKthAncestor(self.parent[node][pos], k - low_bit)


if __name__ == '__main__':
    treeAncestor = TreeAncestor(7, [-1, 0, 0, 1, 1, 2, 2])
    print(treeAncestor.getKthAncestor(3, 1))
    # 返回 1 ，它是 3 的父节点
    print(treeAncestor.getKthAncestor(5, 2))
    # 返回 0 ，它是 5 的祖父节点
    print(treeAncestor.getKthAncestor(6, 3))
    # 返回 -1 因为不存在满足要求的祖先节点
