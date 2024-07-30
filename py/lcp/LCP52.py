"""
 * 欢迎各位勇者来到力扣城，本次试炼主题为「二叉搜索树染色」。
 * 每位勇士面前设有一个二叉搜索树的模型，模型的根节点为 root，树上的各个节点值均不重复。
 * 初始时，所有节点均为蓝色。现在按顺序对这棵二叉树进行若干次操作， ops[i] = [type, x, y] 表示第 i 次操作为：
 * 1、type 等于 0 时，将节点值范围在 [x, y] 的节点均染蓝
 * 2、type 等于 1 时，将节点值范围在 [x, y] 的节点均染红
 * 请返回完成所有染色后，该二叉树中红色节点的数量。
 * 注意：题目保证对于每个操作的 x、y 值定出现在二叉搜索树节点中
 * 提示：
 * 1、1 <= 二叉树节点数量 <= 10^5
 * 2、1 <= ops.length <= 10^5
 * 3、ops[i].length == 3
 * 4、ops[i][0] 仅为 0 or 1
 * 5、0 <= ops[i][1] <= ops[i][2] <= 10^9
 * 6、0 <= 节点值 <= 10^9
 * 链接：https://leetcode.cn/problems/QO5KpG/
"""
import bisect
from typing import List

import sys, os

sys.path.append(os.path.dirname(__file__) + '/../')
from LCUtil import *


class Solution:

    def getNumber(self, root: Optional[TreeNode], ops: List[List[int]]) -> int:
        q, cur = [], root
        nums = []
        while q or cur:
            if cur:
                q.append(cur)
                cur = cur.left
            else:
                cur = q.pop()
                nums.append(cur.val)
                cur = cur.right
        n = len(nums)
        tree = [0 for _ in range(2 << n.bit_length())]
        dirty = [-1 for _ in range(2 << n.bit_length())]

        def push_down(o, l, r):
            if dirty[o] == -1: return
            mid = (l + r) >> 1
            set_value(o * 2 + 1, l, mid, l, mid, dirty[o])
            set_value(o * 2 + 2, mid + 1, r, mid + 1, r, dirty[o])
            dirty[o] = -1

        def set_value(o, l, r, L, R, val):
            # o: 根节点 l：区间左端点 r：区间右端点 LR：更新下标范围 val：更新值
            mid = (l + r) >> 1
            if l == L and r == R:
                tree[o] = val * (R - L + 1)
                dirty[o] = val
                return
            push_down(o, l, r)
            if R <= mid:
                set_value(o * 2 + 1, l, mid, L, R, val)
            elif mid + 1 <= L:
                set_value(o * 2 + 2, mid + 1, r, L, R, val)
            else:
                set_value(o * 2 + 1, l, mid, L, mid, val)
                set_value(o * 2 + 2, mid + 1, r, mid + 1, R, val)
            process(o, l, r)

        def process(o, l, r):
            if l == r: return
            a, b = tree[o * 2 + 1], tree[o * 2 + 2]
            tree[o] = a + b

        for t, x, y in ops:
            if x > y: x, y = y, x
            a, b = bisect.bisect_left(nums, x), bisect.bisect_left(nums, y)
            set_value(0, 0, n - 1, a, b, t)

        return tree[0]


if __name__ == '__main__':
    # 5
    print(Solution().getNumber(stringToTreeNode('[4,2,7,1,null,5,null,null,null,null,6]'),
                               [[1, 1, 5], [0, 4, 5], [1, 5, 7]]))
    # 2
    print(Solution().getNumber(stringToTreeNode('[1, null, 2, null, 3, null, 4, null, 5]'),
                               ops=[[1, 2, 4], [1, 1, 3], [0, 3, 5]]))
    #
    # print(Solution().getNumber())
