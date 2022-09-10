from typing import List
import collections
from collections import deque
'''
给定一个二叉树（具有根结点 root）， 一个目标结点 target ，和一个整数值 k 。
返回到目标结点 target 距离为 k 的所有结点的值的列表。 答案可以以 任何顺序 返回。
提示:
1、节点数在 [1, 500] 范围内
2、0 <= Node.val <= 500
3、Node.val 中所有值 不同
4、目标结点 target 是树上的结点。
5、0 <= k <= 1000
链接：https://leetcode.cn/problems/all-nodes-distance-k-in-binary-tree
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        next_map = collections.defaultdict(list)

        def dfs(root):
            if root.left is not None:
                next_map[root.left.val].append(root.val)
                next_map[root.val].append(root.left.val)
                dfs(root.left)
            if root.right is not None:
                next_map[root.right.val].append(root.val)
                next_map[root.val].append(root.right.val)
                dfs(root.right)
        dfs(root)
        q = deque()
        q.append(target.val)
        visited = set()
        visited.add(target.val)
        n = 0
        while n < k:
            size = len(q)
            for i in range(size):
                cur = q.popleft()
                ns = next_map[cur]
                visited.add(cur)
                for next in ns:
                    if next not in visited:
                        q.append(next)
            n += 1
        return list(q)
